from collections import defaultdict


def create_graph(deps):
    graph = defaultdict(list)
    for dep in deps:
        source, dest = map(int, dep.split("|"))
        graph[dest].append(source)
    return graph


def topological_sort(graph, task):
    '''
    Perform topological sort to reorder the task based on dependencies
    '''
    depends_on = defaultdict(set)
    for node in task:
        for other in task:
            if node != other:
                for dep in graph[node]:
                    if dep in task and dep == other:
                        depends_on[node].add(other)

    result = []
    remaining = set(task)

    while remaining:
        found = False
        for node in list(remaining):
            if not any(other in remaining for other in depends_on[node]):
                result.append(node)
                remaining.remove(node)
                found = True
                break

        if not found:
            first = min(remaining)
            result.append(first)
            remaining.remove(first)

    return result


def check_deps(graph, task):
    '''
    Check if the task is in the correct order based on dependencies
    '''
    pages_done = set()
    pages_needed = set(task)
    for t in task:
        for dep in graph[t]:
            if dep in pages_needed and dep not in pages_done:
                return False
        pages_done.add(t)
    return True


def main():
    file = "input.txt"
    with open(file) as f:
        data = f.read()
    deps, tasks = data.split("\n\n")
    deps = deps.split("\n")
    tasks = tasks.split("\n")
    tasks = [list(map(int, task.split(","))) for task in tasks]
    graph = create_graph(deps)

    middle_number_total_1 = 0
    for task in tasks:
        if check_deps(graph, task):
            middle_number_total_1 += task[len(task)//2]
    print("Part 1 answer:", middle_number_total_1)

    middle_number_total_2 = 0
    for task in tasks:
        if not check_deps(graph, task):
            reordered_task = topological_sort(graph, task)
            middle_number_total_2 += reordered_task[len(reordered_task)//2]
    print("Part 2 answer:", middle_number_total_2)


if __name__ == "__main__":
    main()
