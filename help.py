def get_list(id_folder)
        a = []
        if id_folder is None:
                el = wd
        else:
                el = wd.select_by_id(folder.id)

	if len(el.els) > 0:
		for el in el.els:
			id = id
			name = name
			type = type
			if el.type is a folder:
				child = self.get_list(id)
				a.append(Folder(id=id, name = name, child = child)
			else:
				a.append(Checklist(id=id, name = name)
        return a
