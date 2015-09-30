typedef struct node_obj* NodeOBJ;
NodeOBJ newNodeOBJ(char*, NodeOBJ, unsigned long);
void nodeAddChild(NodeOBJ, NodeOBJ);
void nodeToHTMLTree(NodeOBJ, _Bool);
void deleteNodeOBJ(NodeOBJ);