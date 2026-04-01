class Tag:
    def __init__(self, name, content="", **attributes):
        self._name = name
        self._content = content
        self.__attributes = attributes
        self.__children = []

    def add_child(self, child):
        if hasattr(child, "__str__"):
            self.__children.append(child)
        else:
            raise TypeError("Child must behave like Tag")

    def add_attribute(self):
        attr = ""
        for key, value in self.__attributes.items():
            if key.endswith("_"):
                key = key[:-1]
            attr += f' {key}="{value}"'
        return attr
    
    def __str__(self):
        return self._render()
        
    
    @property
    def name(self):
        return self._name
    
    @property
    def content(self):
        return self._content
    
    @name.setter
    def  name(self, value):
        self._name = value

    @content.setter
    def content(self, value):
        self._content = value

    
    


print(div)
print(div.name)
div.name = "section"
print(div)
