from collections import defaultdict, List

class Solution:
    def has_cycle(self, graph, cur_node, visited, result):
        if visited[cur_node] == 1:
            return False
        if visited[cur_node] == 2:
            return True
        visited[cur_node] = 2
        for next_node in graph[cur_node]:
            if self.has_cycle(graph, next_node, visited, result):
                return True
        visited[cur_node] = 1
        result.append(cur_node)
        return False

    def sortItems(self, n: int, m: int, group: List[int],
                  beforeItems: List[List[int]]) -> List[int]:
        # Map between group_id and item_ids
        group_items_map = defaultdict(list)
        # Visited for items in each group. Will be used later
        visited_item = defaultdict(dict)
        for i in range(n):
            # Assign no-group items to a new group
            if group[i] == -1:
                group[i] = m
                m += 1
            group_items_map[group[i]].append(i)
            visited_item[group[i]][i] = 0

        # key - group_id : value - next_groups
        graph_group = defaultdict(set)
        # key - group_id : value - {key - item_id : value: next_items}
        graph_item = {i: defaultdict(list) for i in range(m)}

        # Create graph for items and groups
        for item_after, before_items in enumerate(beforeItems):
            for item_before in before_items:
                group_before = group[item_before]
                group_after = group[item_after]

                # If two items belong to different groups,
                #   add a dependency between groups
                # Otherwise, add a dependency between items in the same group
                if group_before != group_after:
                    graph_group[group_before].add(group_after)
                else:
                    graph_item[group_before][item_before].append(item_after)

        # Use DFS to find group order
        visited_group = [0] * m
        group_order = []
        for group_id in range(m):
            if self.has_cycle(graph_group, group_id,
                              visited_group, group_order):
                return []

        # Use DFS to find item order in each group
        full_item_order = []
        for group_id in group_order:
            for item_id in group_items_map[group_id]:
                if self.has_cycle(graph_item[group_id], item_id,
                                  visited_item[group_id], full_item_order):
                    return []
        return full_item_order[::-1]