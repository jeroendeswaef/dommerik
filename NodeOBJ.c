#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

#include "NodeOBJ.h"

struct node_obj {
	char* m_tagName;
	char* m_Id;
};

/* Any "class static" vars simply get declared as
static int staticvar;
 * or whatever you like here.
 * Whereas instance variables go in the struct above.
 */

NodeOBJ newNodeOBJ(char* tag_name){
	NodeOBJ node = (NodeOBJ)malloc(sizeof(struct node_obj));
	bzero(node, sizeof(struct node_obj));
	node->m_tagName=tag_name;
	return node;
}

void nodeToHTML(NodeOBJ node){
	printf("TODO: serialize %s\n", node->m_tagName);
}

void deleteNodeOBJ(NodeOBJ node){
	free(node);
}
