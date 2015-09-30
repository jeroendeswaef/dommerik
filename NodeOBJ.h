typedef struct node_obj* NodeOBJ;
NodeOBJ newNodeOBJ(StrMap*, NodeOBJ, unsigned long);
void nodeAddChild(NodeOBJ, NodeOBJ);
void nodeToHTMLTree(NodeOBJ, _Bool);
void deleteNodeOBJ(NodeOBJ);