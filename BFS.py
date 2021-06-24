def bfs (m_dfs, ind, find):
    visited = []
    queue = [ind]
    while queue:
        nodes = queue.pop(0)
        if nodes in m_dfs:
            for neighbours in m_dfs[nodes]:
                if neighbours not in visited:
                    visited.append(neighbours)
                    queue.append(neighbours)
                    if neighbours == enter:
                        print("Nodes is present")
                        break
        elif nodes not in visited:
            visited.append(nodes)


if __name__ == '__main__':
    my_dfs = {'A': ['B', 'F', 'D', 'E'], 'B': ['K', 'J'], 'D': ['G'], 'E': ['C', 'H', 'I'], 'K': ['N', 'M'], 'I': 'L'}
    enter = input("ENter the node you wanna searched : ")
    bfs(my_dfs, 'A', enter)