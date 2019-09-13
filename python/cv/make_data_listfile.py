# -*- coding: utf-8 -* -
'''
将指定目录下的图片整理成文本格式的训练、验证、测试数据列表文件。
目录的格式为：
数据目录/train|val|test/类别名/图片文件
保存的数据列表文件格式为:
文件绝对路径  类别id   类别名称
'''
import os
import glob


def get_categories(datapath):
    assert os.path.exists(datapath), "datapath not exist!"
    categories = os.listdir(datapath)
    category_to_id = {category: id for id, category in enumerate(categories)}
    id_to_category = {category_to_id[category]: category for category in category_to_id}
    return categories, category_to_id, id_to_category


def load_images_to_listfile(data_dir, save_dir, sep=","):
    assert os.path.exists(data_dir), "data sir not exist!"

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    varlid_image_extension = ["jpg", "jpeg", "gif", "png", "bmp"]

    set_list = os.listdir(data_dir)
    set_list = [set_name for set_name in set_list if not set_name.startswith(".")]
    categories, category_to_id, id_to_category = get_categories(os.path.join(data_dir, set_list[0]))

    for set_name in set_list:
        save_file = os.path.join(save_dir, set_name + ".txt")

        filepath_list = []
        for img_ext in varlid_image_extension:
            filepath_list += glob.glob(os.path.join(data_dir, set_name, "*", "*.{}".format(img_ext)))
        sample_list = []
        for filepath in filepath_list:
            cat_name = os.path.basename(os.path.dirname(filepath))
            sample_list.append([os.path.abspath(filepath), str(category_to_id[cat_name]), cat_name])

        with open(save_file, "a+") as wf:
            wf.write("\n".join([sep.join(sample) for sample in sample_list]))

        print("write {} finish".format(set_name + ".txt"))


if __name__ == '__main__':
    data_dir = "/Users/rensike/Work/data/shougang_cold/poc/batch_1"
    save_dir = "/Users/rensike/Work/data/shougang_cold/poc/batch_1_list"
    load_images_to_listfile(data_dir, save_dir)
