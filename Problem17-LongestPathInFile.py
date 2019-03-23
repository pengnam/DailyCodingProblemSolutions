def solution(path):

    # 1. Process to a [(num tabs, length, file or dir) .. ]
    # 2. Perform a "dfs", where if the num_tabs is larger, head front, if equal, head back then front, if less head back
    def process_name(name):
        tabs = name.count("\t")
        is_file = "." in name
        length = len(name) - tabs
        return (tabs, length, is_file)

    names = path.split("\n")
    file_and_dirs = [process_name(name) for name in names]

    node_index = [0]
    def dfs(length, level = 0):
        print(node_index)
        print(level)
        print(length)
        name = names[node_index[0]]
        print(name)
        print("------------")
        result = 0
        while (node_index[0]  < len(file_and_dirs)):
            node = file_and_dirs[node_index[0]]
            if node[2]:#is file
                node_index[0] += 1
                result = max(result, length + node[1] + level)
            elif node[0] == level:
                node_index[0] += 1
                result = max(dfs(length + node[1], level + 1), result)
            elif node[0] < level:
                print("RETURNING")
                return result
        print("Result for:" + name)
        print(result)
        return result
    return dfs(0)



print(solution("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))


