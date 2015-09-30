 #include "NodeOBJ.h"

int main(){
	NodeOBJ obj = newNodeOBJ("div");
	nodeToHTML(obj);
	deleteNodeOBJ(obj);

	return 0;
}

