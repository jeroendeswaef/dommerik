	StrMap* obj1Attr;
	obj1Attr = sm_new(2);
	sm_put(obj1Attr, "_tagName", "div");
	sm_put(obj1Attr, "class", "box");
	NodeOBJ obj1 = newNodeOBJ(obj1Attr, NULL, 1);

	StrMap* obj2Attr;
	obj2Attr = sm_new(3);
	sm_put(obj2Attr, "_tagName", "input");
	sm_put(obj2Attr, "type", "text");
	sm_put(obj2Attr, "name", "myinput");
	NodeOBJ obj2 = newNodeOBJ(obj2Attr, obj1, 0);
	nodeAddChild(obj1, obj2);

	StrMap* obj3Attr;
	obj3Attr = sm_new(3);
	sm_put(obj3Attr, "_tagName", "button");
	sm_put(obj3Attr, "_text", "Click me");
	NodeOBJ obj3 = newNodeOBJ(obj3Attr, obj1, 0);
	nodeAddChild(obj1, obj3);

	nodeToHTMLTree(obj1, 0);

	deleteNodeOBJ(obj1);
	deleteNodeOBJ(obj2);

	sm_delete(obj1Attr);
	sm_delete(obj2Attr);