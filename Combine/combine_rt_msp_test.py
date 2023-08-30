import os
import re
import pandas as pd
import numpy as np


def combine_msp_file(msp_path, out_path):
    """
    FUNCTION:合并msp文件
    """

    # 定义要查找的文件后缀
    file_extension = '/*.msp'

    # 查找文件并将它们合并到一个总文件中
    with open(out_path + '/combine_data.msp', 'w+') as outfile:
        for filename in msp_path:
            with open(filename) as infile:
                outfile.write(infile.read())
            # 在每个文件之间添加分隔符
            # outfile.write('\n')
    outfile.close()

def group_cmp_inf(lines):
    """
    FUNCTION:检索物质名所在行
    """
    group_inf_idx = [i for i, p in enumerate(lines) if 'Name:' in p]
    group_inf_idx.append(len(lines))
    return group_inf_idx

def del_none_ion_cpm(msp, error_df):
    """
    FUNCTION:去除无离子信息的msp
    """
    lines = msp.readlines()
    new_list = [item.replace('NAME:', 'Name:') for item in lines]
    lines = [item.replace("Num peaks:", "Num Peaks:") for item in new_list]
    group_inf_idx = group_cmp_inf(lines)
    del_list = []
    del_none_ion_cpm_list = []
    for j in range(len(group_inf_idx) - 1):
        group_inf = lines[group_inf_idx[j]:group_inf_idx[j + 1]]
        result = [item for item in group_inf if re.match(r'^\d', item)]
        if not result:
            del_none_ion_cpm_list.append(lines[group_inf_idx[j]])
            error_df.loc[len(error_df.index)] = [lines[group_inf_idx[j]].replace('Name: ', ''),
                                                 '该化合物在库中未检索到质谱数据']
            del_list.extend(
                (
                    group_inf_idx[j],
                    group_inf_idx[j + 1],
                )
            )

    del_com = len(del_list) - 1
    while del_com > 0:
        del lines[del_list[del_com - 1]:del_list[del_com]]
        del_com = del_com - 2
    # with open('./del_none_ion_cpm.msp', 'w+') as f:
    #     for p in lines:
    #         f.write(p)
    # f.close()
    return lines, error_df

def Replace_Greek_numbers(lines):
    """
    FUNCTION:将msp库中.alpha.等统一改为alpha
    """
    replacements = {".alpha.": "alpha", ".beta.": "beta", ".gamma.": "gamma", ".delta.": "delta",
                    ".omega.": "omega", ".tau.": "tau"}

    for i in range(len(lines)):
        for old_str, new_str in replacements.items():
            lines[i] = lines[i].replace(old_str, new_str)
            # 将msp库中.alpha.等统一改为alpha
    return lines

def find_insert_position(lst, num):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return left

def Remove_Duplicates(lines, error_df, out_path):
    """
    FUNCTION:msp去重
    """
    # 使用列表推导式和startswith()方法选出以"CAS"开头的字符串
    cas_strings = [s for s in lines if s.startswith('CAS')]

    # 对于选出来的字符串，使用replace()方法删除其中的破折号
    cas_strings_without_dash = [s.replace('-', '') for s in cas_strings]

    # 使用正则表达式提取每个字符串中的第一组连续的数字，并将其转换为整数
    cas_numbers = [int(re.findall(r'\d+', s)[0]) for s in cas_strings_without_dash]

    # 找到每个"CAS"字符串在原来的列表中的索引
    cas_indices = [i for i, s in enumerate(lines) if s in cas_strings]

    j_list = sorted(set(cas_numbers))
    del_list = []
    group_inf_idx = group_cmp_inf(lines)

    for j in j_list:
        index_list = [i for i in range(len(cas_numbers)) if cas_numbers[i] == j]
        index_list = index_list[1:]
        for idx in index_list:
            position = find_insert_position(group_inf_idx, cas_indices[idx])
            error_df.loc[len(error_df.index)] = [lines[group_inf_idx[position - 1]].replace('Name: ', ''),
                                                 '该化合物在库中出现重复']
            del_list.extend(
                (
                    group_inf_idx[position - 1],
                    group_inf_idx[position]
                )
            )

    del_list.sort()
    del_com = len(del_list) - 1
    while del_com > 0:
        if del_com < len(lines):
            del lines[del_list[del_com - 1]:del_list[del_com]]
        del_com = del_com - 2
    # print('去重后的物质数量：', len(group_cmp_inf(lines)))

    group_inf_idx = group_cmp_inf(lines)
    del_list_n = []
    n_all_list = [lines[s].replace('Name: ', '') for s in group_inf_idx[:-1]]
    n_list = sorted(set(n_all_list))

    for n in n_list:
        index_list = [i for i in range(len(n_all_list)) if n_all_list[i] == n]
        index_list = index_list[1:]
        for idx in index_list:
            error_df.loc[len(error_df.index)] = [lines[group_inf_idx[idx]].replace('Name: ', ''),
                                                 '该化合物在库中出现重复']
            del_list_n.extend(
                (
                    group_inf_idx[idx],
                    group_inf_idx[idx + 1]
                )
            )

    del_list_n.sort()
    del_com = len(del_list_n) - 1
    while del_com > 0:
        if del_com < len(lines):
            del lines[del_list_n[del_com - 1]:del_list_n[del_com]]
        del_com = del_com - 2
    with open(out_path + '/Remove_Duplicates.msp', 'w+') as f:
        for p in lines:
            f.write(p)
    f.close()
    return lines, error_df

def combine_RT_file(rt_path, out_path, file_suffixes=None, merged_file_name=None):
    """
    FUNCTION:转换样本RT-RI
    file_suffixes：定义要读取的文件后缀
    merged_file_name：定义合并后的文件名
    return:合并后的RT库
    """
    # # 定义要读取的文件后缀
    # if file_suffixes is None:
    #     file_suffixes = [".xlsx", ".txt", ".csv"]
    #
    # # 定义合并后的文件名
    # if merged_file_name is None:
    #     merged_file_name = "combine_RT_file.xlsx"
    # # 定义一个空的DataFrame对象
    # merged_df = pd.DataFrame()
    #
    # # 遍历所有文件后缀，并读取所有符合后缀的文件
    # for file_suffix in file_suffixes:
    #     # 获取当前目录下所有符合后缀的文件路径
    #     file_paths = glob.glob(rt_path + "/*" + file_suffix)
    #     print(rt_path + "/*" + file_suffix)
    #     # 遍历所有符合后缀的文件，并将它们读取到DataFrame对象中
    #     for file_path in file_paths:
    #
    #         if file_suffix == ".xlsx":
    #             df = pd.read_excel(file_path)
    #         elif file_suffix == ".txt":
    #             df = pd.read_csv(file_path, sep="\t")
    #         elif file_suffix == ".csv":
    #             df = pd.read_csv(file_path)
    #         merged_df = pd.concat([merged_df, df], ignore_index=True)
    #
    #         # 删除已经合并的文件
    #         # os.remove(file_path)
    #
    # # 将合并后的数据写入Excel文件中
    # merged_df.to_excel(rt_path + '/' + merged_file_name, index=False)

    merged_df = pd.DataFrame()
    if merged_file_name is None:
        merged_file_name = "combine_RT_file.xlsx"
    for file_path in rt_path:
        if file_path.split(".")[-1] == "xlsx":
            df = pd.read_excel(file_path)
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif file_path.split(".")[-1] == "txt":
            df = pd.read_csv(file_path, sep="\t")
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        elif file_path.split(".")[-1] == "csv":
            df = pd.read_csv(file_path)
            merged_df = pd.concat([merged_df, df], ignore_index=True)

        # 删除已经合并的文件
        # os.remove(file_path)

    merged_df.to_excel(out_path + '/' + merged_file_name, index=False)

def Remove_Duplicates_RT(msp, RT_data, out_path, check_latin):
    error_df = pd.DataFrame(columns=["Name", "RT", "错误", "NIST首名"])
    for index_1, row in RT_data.iterrows():
        try:
            float(row[1])
        except Exception:
            RT_data.drop(index=index_1, inplace=True)
            error_df.loc[len(error_df)] = [row[0], row[1], "RT数值有误", np.nan]
    RT_data['RT'] = RT_data['RT'].astype('float')
    # print("去掉有误RT后长度", len(RT_data))

    replacements = {".alpha.": "alpha", ".beta.": "beta", ".gamma.": "gamma", ".delta.": "delta",
                    ".omega.": "omega", ".tau.": "tau"}
    if check_latin:
        for i in range(RT_data.shape[0]):
            for old_str, new_str in replacements.items():
                RT_data.iloc[i, 0] = RT_data.iloc[i, 0].replace(old_str, new_str)
                # 将RT列表中.alpha.等统一改为alpha

    lines = msp.readlines()
    new_list = [item.replace('NAME:', 'Name:') for item in lines]
    lines = [item.replace("Num peaks:", "Num Peaks:") for item in new_list]
    lines = Replace_Greek_numbers(lines)

    name_df = pd.DataFrame(columns=["Name", "Index"])
    for i in lines:
        if "Name" in i:
            name_df.loc[len(name_df)] = [i.split("Name:")[1].strip(), lines.index(i)]
    name_df = name_df.drop_duplicates(subset=['Name'], keep='first')

    synon_df = pd.DataFrame(columns=["Synon", "Index"])
    for i in lines:
        if "Synon" in i:
            synon_df.loc[len(synon_df)] = [i.split("Synon:")[1].strip(), lines.index(i)]

    name_index_list = name_df["Index"].values.tolist()
    for index_1, row in RT_data.iterrows():
        if row[0] not in name_df["Name"].values.tolist():
            # print(row[0], "不在NIST首名列表")
            if row[0] not in synon_df["Synon"].values.tolist():
                # print(row[0], "不在NIST库")
                error_df.loc[len(error_df)] = [row[0], row[1], "不在MSP库中", np.nan]
                RT_data.drop(index=index_1, inplace=True)
            else:
                temp_list = []
                synon_index = synon_df.loc[synon_df["Synon"] == row[0], "Index"].tolist()[0]
                if temp_list := [
                    x for x in name_index_list if x < synon_index
                ]:
                    # print(row[0], "在同义名列表")
                    # print("*"*30)
                    # print("改名前", row[0])
                    name_index = max(temp_list)
                    error_df.loc[len(error_df)] = [row[0], row[1], "已改同义名为NIST首名",
                                                   name_df.loc[
                                                       name_df["Index"] == name_index, "Name"].values.tolist()[
                                                       0]]
                    # print(name_df.loc[name_df["Index"] == name_index, "Name"])
                    RT_data.loc[index_1, "Name"] = \
                        name_df.loc[name_df["Index"] == name_index, "Name"].values.tolist()[
                            0]
                else:
                    error_df.loc[len(error_df)] = [row[0], row[1], "搜索同义名时出错", np.nan]
                    RT_data.drop(index=index_1, inplace=True)
    # print("去掉不在msp库物质长度", len(RT_data))

    duplicated_names = RT_data[RT_data.duplicated(['Name'], keep="first")]['Name']
    for name in duplicated_names:
        rt_values = RT_data.loc[RT_data['Name'] == name, 'RT'].tolist()
        name_rt_df = pd.DataFrame({'Name': [name] * len(rt_values), 'RT': rt_values, "错误": "物质名重复"})
        error_df = pd.concat([error_df, name_rt_df], ignore_index=True)

    error_df.sort_values(by="Name", inplace=True, ascending=True)
    RT_data = RT_data.drop_duplicates(subset=['Name'], keep='first')
    RT_data = RT_data.sort_values(by="RT", ascending=True)

    # print("去掉重复名字长度", len(RT_data))

    # RT_data.to_excel(r"./{}.xlsx".format("New_RT_list"), index=True)
    # error_df.to_excel('./Error_info.xlsx', index=True)

    return RT_data, error_df

def inspection_result(path_rt, RT_data, standard_df, RI_alert_lower_limit, RI_alert_upper_limit,
                      RI_threshold_value, ri_window_scale, RT_lower_limit,
                      RT_upper_limit, RI_lower_limit, RI_upper_limit, change_RT_to_theoretical_RT):
    """
    FUNCTION:转换样本RT-RI
    RT_data: RT库
    msp: MSP库
    RI_lower_limit: RI警告下限
    RI_upper_limit: RI警告上限
    RI_threshold_value:  RI阈值
    return:检验结果
    """
    msp = open(path_rt, "r")
    lines = msp.readlines()
    new_list = [item.replace('NAME:', 'Name:') for item in lines]
    lines = [item.replace("Num peaks:", "Num Peaks:") for item in new_list]
    group_inf_idx = group_cmp_inf(lines)
    RI_df = pd.DataFrame(columns=['Name', 'RI_msp'])
    for j in range(len(group_inf_idx) - 1):
        group_inf = lines[group_inf_idx[j]:group_inf_idx[j + 1]]
        # 定义要匹配的字符串前缀
        prefixes = [r'SemiStdNP=\d+', r'RI:\d+\n']
        # 定义正则表达式
        pattern = "|".join(prefixes)
        for string in group_inf:
            if 'Name:' in string:
                RI_list = [string.replace('Name: ', '')]
            if matches := re.findall(pattern, string):
                RI_list.extend([int(re.findall(r"\d+", match)[0]) for match in matches])
                # print(RI_list)
                RI_df.loc[len(RI_df.index)] = RI_list
    RI_df['Name'] = RI_df['Name'].str.rstrip('\n')

    combine_df = pd.merge(RT_data, RI_df, on='Name', how='outer')
    combine_df['RI_input'] = combine_df.apply(
        lambda row: RT_to_Kovats_RI_transform(row['RT'], standard_df, RI_lower_limit, RI_upper_limit),
        axis=1)

    combine_df['Alert'] = combine_df.apply(
        lambda row: alert_ri_offset_is_too_large(row['RI_msp'], row['RI_input'], RI_alert_lower_limit,
                                                      RI_alert_upper_limit, RI_threshold_value, ri_window_scale), axis=1)

    combine_df = combine_df[['Name', 'RT', 'RI_msp', 'RI_input', 'Alert']]

    for i, combine_df_row in combine_df.iterrows():
        if np.isnan(combine_df_row[1]):
            combine_df.loc[i, "RT"] = Kovats_RI_to_RT_transform(combine_df_row[2], standard_df,
                                                                     RT_lower_limit, RT_upper_limit)
            combine_df.loc[i, "Alert"] = 'rt_is_in_silico'
        if combine_df.loc[i, "Alert"] == "RI_offset_is_too_large":
            if change_RT_to_theoretical_RT == False:
                combine_df.loc[i, "RT_in_silico"] = Kovats_RI_to_RT_transform(combine_df_row[2], standard_df,
                                                                              RT_lower_limit,
                                                                              RT_upper_limit)
            elif change_RT_to_theoretical_RT == True:
                combine_df.loc[i, "RT"] = Kovats_RI_to_RT_transform(combine_df_row[2], standard_df,
                                                                    RT_lower_limit,
                                                                    RT_upper_limit)
    # combine_df.sort_values(by="RT", inplace=True, ascending=True)
    combine_df = combine_df.drop_duplicates(subset=['Name'], keep='first')
    print('去重后含有RI物质的数量：', combine_df.shape[0])
    combine_df = combine_df.sort_values(by="RT", ascending=True)
    combine_df.set_index(['Name'], inplace=True)
    combine_df.dropna(how='all', subset=['RT', 'RI_msp'], inplace=True)

    return combine_df

def alert_ri_offset_is_too_large(RI_msp, RI_input, RI_alert_lower_limit, RI_alert_upper_limit, RI_threshold_value,
                                 ri_window_scale):
    # if RI_alert_lower_limit is None:
    #     RI_alert_lower_limit = 600
    # if RI_alert_upper_limit is None:
    #     RI_alert_upper_limit = 2000
    # if RI_threshold_value is None:
    #     RI_threshold_value = 40
    # if ri_window_scale is None:
    #     ri_window_scale = 5
    if type(RI_input) != str:
        if RI_alert_lower_limit < RI_input < RI_alert_upper_limit and abs(
                RI_msp - RI_input) > RI_threshold_value + ri_window_scale * 0.01 * RI_input:
            return "RI_offset_is_too_large"

def Kovats_RI_to_RT_transform(ri_sample, standard_df, RT_lower_limit, RT_upper_limit):
    """
    FUNCTION:转换样本RT-RI
    ri_sample：样本RI
    standard_df：标品RT-RI
    return:样本RT
    """
    # if RT_lower_limit is None:
    #     RT_lower_limit = 0
    # if RT_upper_limit is None:
    #     RT_upper_limit = 68.8
    prev_rows = standard_df.loc[(standard_df['RI'] < ri_sample)].tail(1)
    next_rows = standard_df.loc[(standard_df['RI'] > ri_sample)].head(1)
    if prev_rows.shape[0] == 0:
        df_sort = standard_df.sort_values('RT (min)', ascending=True).head(2)
    elif next_rows.shape[0] == 0:
        df_sort = standard_df.sort_values('RT (min)', ascending=True).tail(2)
    else:
        df_sort = pd.concat([prev_rows, next_rows])
    RI_low = min(df_sort['RI'])
    RI_high = max(df_sort['RI'])
    RT_low = min(df_sort['RT (min)'])
    RT_high = max(df_sort['RT (min)'])
    rt_sample = RT_low + (ri_sample - RI_low) * (RT_high - RT_low) / (RI_high - RI_low)
    if rt_sample < RT_lower_limit:
        return RT_lower_limit
    elif rt_sample > RT_upper_limit:
        return RT_upper_limit
    else:
        return rt_sample

def RT_to_Kovats_RI_transform(rt_sample, standard_df, RI_lower_limit, RI_upper_limit):
    """
    FUNCTION:转换样本RT-RI
    rt_sample：样本RT
    standard_df：标品RT-RI
    return:样本RI
    """
    # if RI_lower_limit is None:
    #     RI_lower_limit = 0
    # if RI_upper_limit is None:
    #     RI_upper_limit = 3000
    if np.isnan(rt_sample):
        return "未检索到实测rt内容"
    prev_rows = standard_df.loc[(standard_df['RT (min)'] < rt_sample)].tail(1)
    next_rows = standard_df.loc[(standard_df['RT (min)'] >= rt_sample)].head(1)
    if prev_rows.shape[0] == 0:
        df_sort = standard_df.sort_values('RT (min)', ascending=True).head(2)
    elif next_rows.shape[0] == 0:
        df_sort = standard_df.sort_values('RT (min)', ascending=True).tail(2)
    else:
        df_sort = pd.concat([prev_rows, next_rows])
    RI_low = min(df_sort['RI'])
    RI_high = max(df_sort['RI'])
    RT_low = min(df_sort['RT (min)'])
    RT_high = max(df_sort['RT (min)'])
    ri_sample = round(RI_low + (RI_high - RI_low) * (rt_sample - RT_low) / (RT_high - RT_low))
    if ri_sample < RI_lower_limit:
        return RI_lower_limit
    elif ri_sample > RI_upper_limit:
        return RI_upper_limit
    else:
        return ri_sample



def read_msp(msp_file):
    msp_file = open(msp_file, "r")
    list_1 = msp_file.readlines()
    # print(list_1)
    new_list = [item.replace('NAME:', 'Name:') for item in list_1]
    list_1 = [item.replace("Num peaks:", "Num Peaks:") for item in new_list]
    # print(list_1)
    lists = str(list_1)
    lines = lists.split("Name: ")
    meta = {}
    for l in lines:
        line1 = l.strip().split("\\n")
        # print(line1)
        name_1 = line1[0]
        # print("name = ", name_1)
        line2 = l.strip().split("Num Peaks:")
        ion_intens_dic = {}
        # print("line2 = ", line2)
        if len(line2) > 1:
            if ';' in line2[1]:
                # 使用正则表达式匹配数字对
                matches = re.findall(r"(\d+) (\d+);", line2[1])
                # 创建字典
                ion_intens_dic = {}
                for key, value in matches:
                    key = round(float(key))
                    value = int(value)
                    if key in ion_intens_dic:
                        ion_intens_dic[key] = max(ion_intens_dic[key], value)
                    else:
                        ion_intens_dic[key] = value

            elif '\\t' in line2[1]:
                line3 = line2[1].split("\\n', '")[1:-2]
                for ion in line3:
                    ion1 = ion.split("\\t")
                    # print("ion1 = ", ion1)
                    if len(ion1) == 2 and is_number(ion1[0]) and is_number(ion1[1]):
                        key = round(float(ion1[0]))
                        value = float(ion1[1])
                        if key in ion_intens_dic:
                            ion_intens_dic[key] = max(ion_intens_dic[key], value)
                        else:
                            ion_intens_dic[key] = value
            elif '\\n' in line2[1]:
                line3 = line2[1].split("\\n', '")[1:-2]
                for ion in line3:
                    ion1 = ion.split(" ")
                    # print("ion1 = ", ion1)
                    if len(ion1) == 2 and is_number(ion1[0]) and is_number(ion1[1]):
                        key = round(float(ion1[0]))
                        value = float(ion1[1])
                        if key in ion_intens_dic:
                            ion_intens_dic[key] = max(ion_intens_dic[key], value)
                        else:
                            ion_intens_dic[key] = value
            else:
                print('格式无法识别')
                # print("ion_intens_dic = ", ion_intens_dic)
        meta[name_1] = ion_intens_dic

    return meta

def is_number(s):
    """
    判断字符串 s 是否为数字
    """
    pattern = r'^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$'
    return bool(re.match(pattern, s))


def dot_product_distance(p, q):

    if (np.sum(p)) == 0 or (np.sum(q)) == 0:
        score = 0
    else:
        score = np.power(np.sum(q * p), 2) / \
                (np.sum(np.power(q, 2)) * np.sum(np.power(p, 2)))
    return score

def weighted_dot_product_distance(compare_df, fr_factor):

    # print("debug compare_df = ")
    # print(compare_df)
    m_q = pd.Series(compare_df.index)
    m_q = m_q.astype(float)
    # m_q是df的index，是输入的离子
    # print("debug m_q = ")
    # print(m_q)
    i_q = np.array(compare_df.iloc[:, 0])
    # i_q是df的第一列，是实测响应
    # 后续i_q与m_q要相乘，只有array或Series才可以相乘，因此要把df转为array
    # print("debug i_q = ")
    # print(i_q)
    i_r = np.array(compare_df.iloc[:, 1])
    # i_r是df的第二列，是lib响应
    # print("debug i_r = ")
    # print(i_r)
    k = 0.5
    # NIST的k=0.5，改为1可提高丰度比的权重
    l = 2
    w_q = np.power(i_q, k) * np.power(m_q, l)
    # print("debug w_q = ")
    # print(w_q)
    # print(type(w_q))
    w_r = np.power(i_r, k) * np.power(m_q, l)
    # print("debug w_r = ")
    # print(w_r)

    # 如果组某离子或所有离子读数为0，该步也可正常计算
    ss = dot_product_distance(w_q, w_r)
    # print("debug ss = ", ss)
    shared_spec = np.vstack((i_q, i_r))
    shared_spec = pd.DataFrame(shared_spec)
    shared_spec = shared_spec.loc[:, (shared_spec != 0).all(axis=0)]
    # print("debug_shared_spec = ", shared_spec)
    # 取共有离子
    m = int(shared_spec.shape[1])
    # print("debug_m = ", m)
    # 如果要提高丰度比的权重，即增加m，那么要在该处：composite_score = ((NU*ss) + (m*ave_FR)) / (NU + m)增加m，因为下面有个m是否大于等于2的判断
    if m >= fr_factor:
        FR = 0
        for i in range(1, m):
            # df.iat中，行数在前，列数在后，取值时0是第一行/列，因此range是1到n
            # range中1, n,包含1，但不包含n，最大n-1
            s = (shared_spec.iat[0, i] / shared_spec.iat[0, (i - 1)]) * (
                    shared_spec.iat[1, (i - 1)] / shared_spec.iat[1, i])
            if s > 1:
                s = 1 / s
            FR = FR + s
        ave_FR = FR / (m - 1)
        NU = int(len(compare_df))
        # 原array中行数是物质包含的离子数
        composite_score = ((NU * ss) + (m * ave_FR)) / (NU + m)
    else:
        composite_score = ss

    return composite_score


#
# def Main(msp_path, rt_path, ri_path, RI_alert_lower_limit, RI_alert_upper_limit,
#          RI_threshold_value, ri_window_scale, RT_lower_limit, RT_upper_limit, RI_lower_limit, RI_upper_limit,
#          check_RT, check_latin, out_path):
#     combine_msp_file(msp_path, out_path)
#
#     path_msp = out_path + "/combine_data.msp"
#     with open(path_msp, "r") as msp:
#         error_df = pd.DataFrame(columns=['Name', 'reason'])
#         lines, error_df = del_none_ion_cpm(msp, error_df)
#         new_list = [item.replace('NAME:', 'Name:') for item in lines]
#         lines = [item.replace("Num peaks:", "Num Peaks:") for item in new_list]
#         if check_latin:
#             lines = Replace_Greek_numbers(lines)
#         lines, error_df = Remove_Duplicates(lines, error_df, out_path)
#         error_df = error_df.applymap(lambda x: x.strip())
#         error_df.to_excel(out_path + '/error_df.xlsx', index=False)
#
#     combine_RT_file(rt_path, out_path)
#     path_rt = out_path + "/Remove_Duplicates.msp"
#
#     msp = open(path_rt, "r")
#     try:
#         RT_data_file = out_path + "/combine_RT_file.xlsx"
#         if os.path.exists(RT_data_file):
#             RT_data = pd.read_excel(RT_data_file, header=0)
#         if RT_data.empty:
#             data = np.empty((0, 2))
#             RT_data = pd.DataFrame(data, columns=['Name', 'RT'])
#         RT_data, error_df = Remove_Duplicates_RT(msp, RT_data, out_path, check_latin)
#     finally:
#         msp.close()
#     msp = open(path_rt, "r")
#     try:
#         standard_df = pd.read_csv(ri_path, sep=",")
#         combine_df = inspection_result(path_rt, RT_data, standard_df, RI_alert_lower_limit,
#                                             RI_alert_upper_limit,
#                                             RI_threshold_value, ri_window_scale, RT_lower_limit, RT_upper_limit,
#                                             RI_lower_limit, RI_upper_limit, check_RT)
#         combine_df.to_excel(out_path + '/New_RT_list.xlsx', index=True)
#     finally:
#         msp.close()
#     # os.remove(out_path + "/combine_data.msp")
#     # os.remove(out_path + "/combine_RT_file.xlsx")



msp_path = ["../combine_input/NIST示例库.msp", "../combine_input/安捷伦示例库.MSP"]
rt_path = ["../combine_input/New_RT_list_0323.xlsx"]
ri_path = "../combine_input/0413.csv"
RI_alert_lower_limit = 600
RI_alert_upper_limit = 2000
RI_threshold_value = 40
ri_window_scale = 5
RT_lower_limit = 0
RT_upper_limit = 68.8
RI_lower_limit = 0
RI_upper_limit = 3000
change_RT_to_theoretical_RT = True
check_latin = True
out_path = "../combine_input/results"


# Main(msp_path, rt_path, ri_path, RI_alert_lower_limit, RI_alert_upper_limit,
#              RI_threshold_value, ri_window_scale, RT_lower_limit, RT_upper_limit, RI_lower_limit, RI_upper_limit,
#              change_RT_to_theoretical_RT, check_latin, out_path)


combine_msp_file(msp_path, out_path)

path_msp = out_path + "/combine_data.msp"
with open(path_msp, "r") as msp:
    error_df = pd.DataFrame(columns=['Name', 'reason'])
    lines, error_df = del_none_ion_cpm(msp, error_df)
    new_list = [item.replace('NAME:', 'Name:') for item in lines]
    lines = [item.replace("Num peaks:", "Num Peaks:") for item in new_list]
    if check_latin:
        lines = Replace_Greek_numbers(lines)

    lines, error_df = Remove_Duplicates(lines, error_df, out_path)
    error_df = error_df.applymap(lambda x: x.strip())
    error_df.to_excel(out_path + '/error_df.xlsx', index=False)

combine_RT_file(rt_path, out_path)
path_rt = out_path + "/Remove_Duplicates.msp"

msp = open(path_rt, "r")
try:
    RT_data_file = out_path + "/combine_RT_file.xlsx"
    if os.path.exists(RT_data_file):
        RT_data = pd.read_excel(RT_data_file, header=0)
    if RT_data.empty:
        data = np.empty((0, 2))
        RT_data = pd.DataFrame(data, columns=['Name', 'RT'])
    RT_data, error_df = Remove_Duplicates_RT(msp, RT_data, out_path, check_latin)
finally:
    msp.close()
msp = open(path_rt, "r")
try:
    standard_df = pd.read_csv(ri_path, sep=",")
    combine_df = inspection_result(path_rt, RT_data, standard_df, RI_alert_lower_limit,
                                        RI_alert_upper_limit,
                                        RI_threshold_value, ri_window_scale, RT_lower_limit, RT_upper_limit,
                                        RI_lower_limit, RI_upper_limit, change_RT_to_theoretical_RT)
    combine_df.to_excel(out_path + '/New_RT_list.xlsx', index=True)
finally:
    msp.close()


is_input_unknow = True



if is_input_unknow:
    unknow_msp_path = "../combine_input/unknow_test.msp"
    unknow_rt_path = "../combine_input/unknown_test.xlsx"
    window = 2
    similarity_score_threshold = 1
    meta = read_msp(out_path + "/Remove_Duplicates.msp")
    unknow_rt = pd.read_excel(unknow_rt_path, header=0)
    unknow_meta = read_msp(unknow_msp_path)
    remove_duplicates_lines = open(out_path + "/Remove_Duplicates.msp").readlines()
    unknow_lines = open(unknow_msp_path).readlines()
    unknow_lines = [item.replace('NAME:', 'Name:') for item in unknow_lines]
    unknow_lines = [item.replace("Num peaks:", "Num Peaks:") for item in unknow_lines]
    unknow_group_inf_idx = group_cmp_inf(unknow_lines)
    print(unknow_group_inf_idx)
    add_unknown_list = []
    for index, row in unknow_rt.iterrows():
        name = row[0]
        rt = row[1]
        print("****************", name)
        window_minute_name = combine_df[(combine_df.iloc[:, 0] >= rt-window) & (combine_df.iloc[:, 0] <= rt+window)].index
        unknow_ms_df = pd.DataFrame(list(unknow_meta[name].items()), columns=['ion', 'intensity'])
        name_index = unknow_lines.index("Name: " + name + "\n")
        print("name_index-", name_index)
        next_name_index = unknow_group_inf_idx[unknow_group_inf_idx.index(name_index) + 1]
        print("next_name_index-", next_name_index)
        name_lines = unknow_lines[name_index:next_name_index]
        for m in window_minute_name:
            m_df = pd.DataFrame(list(meta[m].items()), columns=['ion', 'intensity'])
            merged_df = pd.merge(unknow_ms_df, m_df, on='ion', how='inner')
            score = weighted_dot_product_distance(merged_df, 2)
            print("score:", score)
            if score > similarity_score_threshold:
                break
        else:
            add_unknown_list.append(name)
            remove_duplicates_lines = remove_duplicates_lines + name_lines

    with open(out_path + '/Remove_Duplicates_new.msp', 'w+') as f:
        for p in remove_duplicates_lines:
            f.write(p)

    if add_unknown_list != []:

        path_rt = out_path + "/Remove_Duplicates_new.msp"
        msp = open(path_rt, "r")
        try:
            RT_data_file = out_path + "/combine_RT_file.xlsx"
            if os.path.exists(RT_data_file):
                RT_data = pd.read_excel(RT_data_file, header=0)
            if RT_data.empty:
                data = np.empty((0, 2))
                RT_data = pd.DataFrame(data, columns=['Name', 'RT'])
            RT_data, error_df = Remove_Duplicates_RT(msp, RT_data, out_path, check_latin)
        finally:
            msp.close()
        msp = open(path_rt, "r")
        for i in add_unknown_list:

            RT_data = RT_data.append(unknow_rt[unknow_rt["Name"]==i], ignore_index=True)

        try:
            standard_df = pd.read_csv(ri_path, sep=",")
            combine_df = inspection_result(path_rt, RT_data, standard_df, RI_alert_lower_limit,
                                           RI_alert_upper_limit,
                                           RI_threshold_value, ri_window_scale, RT_lower_limit, RT_upper_limit,
                                           RI_lower_limit, RI_upper_limit, change_RT_to_theoretical_RT)
            combine_df.to_excel(out_path + '/New_RT_list_new.xlsx', index=True)
        finally:
            msp.close()
print("all done")