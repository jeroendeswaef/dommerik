#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "NodeOBJ.h"

struct node_obj {
	char* m_tagName;
	char* m_Id;
	NodeOBJ m_parent;
	NodeOBJ* m_children;
	unsigned long m_childrenCnt;
	int m_depth;
};

void print_with_indent(int indent, char * string) {
    printf("%*s" "%s", indent, " ", string); 
}

/* Any "class static" vars simply get declared as static int staticvar;
 * or whatever you like here.
 * Whereas instance variables go in the struct above.
 */

NodeOBJ newNodeOBJ(char* tag_name, NodeOBJ parent, unsigned long expected_children_cnt) {
	NodeOBJ node = (NodeOBJ)malloc(sizeof(struct node_obj));
	bzero(node, sizeof(struct node_obj));
	node->m_tagName = tag_name;
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

void nodeToHTML(NodeOBJ node, _Bool prettyPrint){
	char str[80];
	sprintf(str, "<%s />%s", node->m_tagName, (prettyPrint ? "\n" : ""));
	if (prettyPrint) {
		print_with_indent(node->m_depth * 4, str);
	} else {
		printf(str);
	}
}

void nodeToHTMLTree(NodeOBJ node, _Bool prettyPrint) {
	nodeToHTML(node, prettyPrint);
	for(unsigned long i = 0; i < node-> m_childrenCnt; i++) {
		nodeToHTML(node->m_children[i], prettyPrint);
	}
}

void deleteNodeOBJ(NodeOBJ node){
	free(node);
}
