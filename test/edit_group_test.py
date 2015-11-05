from model.group import Group
import random
__author__ = 'Pysarev'


def test_edit_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Edit_test"))
    old_groups = db.get_group_list()
    old_group=random.choice(old_groups)
    edit_group = Group(name="edited2", footer="edited2")
    edit_group.id = old_group.id
    app.group.edit_group_by_id(edit_group.id, edit_group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups_to_compare = [edit_group if group.id == edit_group.id else group for group in old_groups]
    print (old_groups_to_compare)
    print (new_groups)
    assert old_groups_to_compare == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        ui_list = map(clean, new_groups)
        print(ui_list)
        assert sorted(ui_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)