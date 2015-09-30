#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "strmap.h"
#include "NodeOBJ.h"

struct node_obj {
	StrMap* m_attributes;
	NodeOBJ m_parent;
	NodeOBJ* m_children;
	unsigned long m_childrenCnt;
	int m_depth;
};

static void add_attributes(const char *key, const char *value, const void *obj) {
	char* charObj = (char*)obj;
	// _xxx attributes are used for other element info, not only html attributes
	if (key[0] != '_') {
		unsigned int len = strlen(charObj);
		if (len > 0) {
			charObj[len] = ' ';
			charObj[len + 1] = '\0'; 
		}
	    sprintf(charObj, "%s%s=\"%s\"", charObj, key, value);
	}
}

/* Any "class static" vars simply get declared as static int staticvar;
 * or whatever you like here.
 * Whereas instance variables go in the struct above.
 */

NodeOBJ newNodeOBJ(StrMap* attributes, NodeOBJ parent, unsigned long expected_children_cnt) {
	NodeOBJ node = (NodeOBJ)malloc(sizeof(struct node_obj));
	bzero(node, sizeof(struct node_obj));
	node->m_attributes = attributes;
	node->m_parent = parent;
	if (expected_children_cnt > 0) {
		node->m_children = malloc(expected_children_cnt * sizeof(NodeOBJ));
	} 
	node->m_childrenCnt = 0;
	if (parent != NULL) {
		node->m_depth = parent->m_depth + 1;
	} else {
		node->m_depth = 0;
	}
	return node;
}

void nodeAddChild(NodeOBJ parent, NodeOBJ child) {
	parent->m_children[parent->m_childrenCnt++] = child;
}

void nodeToHTML(NodeOBJ node, _Bool prettyPrint, char* startTag, char* endTag){
	char attrBuf[120];
	char tagBuf[20];
	char innerTextBuf[100];
	attrBuf[0] = '\0';
	tagBuf[0] = '\0';
	innerTextBuf[0] = '\0';

	sm_get(node->m_attributes, "_tagName", tagBuf, sizeof(tagBuf));
	sm_get(node->m_attributes, "_text", innerTextBuf, sizeof(innerTextBuf));
	sm_enum(node->m_attributes, add_attributes, attrBuf);
	
	int indent = (prettyPrint ? node->m_depth * 4 : 0);
	if (indent > 0) {
		sprintf(startTag, "%*s<%s %s>%s", indent, " ", tagBuf, attrBuf, innerTextBuf);
		if (node-> m_childrenCnt > 0) {
			sprintf(endTag, "%*s</%s>", indent, " ", tagBuf);
		} else {
			sprintf(endTag, "</%s>", tagBuf);
		}
	} else {
		sprintf(startTag, "<%s %s>%s", tagBuf, attrBuf, innerTextBuf);
		sprintf(endTag, "</%s>", tagBuf);
	}
}

void nodeToHTMLTree(NodeOBJ node, _Bool prettyPrint) {
	char startTagBuf[200];
	char endTagBuf[20];
	startTagBuf[0] = '\0';
	endTagBuf[0] = '\0';
	nodeToHTML(node, prettyPrint, startTagBuf, endTagBuf);
	printf(strcat(startTagBuf, (prettyPrint && node-> m_childrenCnt > 0 ? "\n" : "")));
	for(unsigned long i = 0; i < node-> m_childrenCnt; i++) {
		nodeToHTMLTree(node->m_children[i], prettyPrint);
	}
	printf(strcat(endTagBuf, (prettyPrint ? "\n" : "")));
}

void deleteNodeOBJ(NodeOBJ node){
	free(node);
}
