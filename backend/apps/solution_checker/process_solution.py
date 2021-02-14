import time

from apps.solution_checker.tasks import check_solution


def post_solution(solution: str) -> int:
    id_ = int(time.time() * 1000)

    check_solution.delay(solution=solution, id_=id_)

    return id_
