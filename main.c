#include <string.h>

#include "NodeOBJ.h"

int main(){
	NodeOBJ obj = newNodeOBJ("div", NULL, 1);
	NodeOBJ obj2 = newNodeOBJ("div", obj, 0);

	nodeAddChild(obj, obj2);

	nodeToHTMLTree(obj, 1);
	//nodeToHTML(obj2);

	deleteNodeOBJ(obj);
	deleteNodeOBJ(obj2);

	return 0;
}

