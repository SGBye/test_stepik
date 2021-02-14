import random
import time
from typing import Tuple

from apps.core.models import Solution
from apps.solution_checker.tasks import check_solution


def post_solution(solution: str) -> int:
    id_ = int(time.time() * 1000)

    check_solution.delay(solution)

    return id_


def get_solution(id_: int) -> Tuple[int, str]:
    status = random.choice([*['evaluation'] * 10, 'correct', 'wrong'])

    return id_, status


def send_solution_callback(status: str, id_: int):
    """
    function for sending callback if it's a different service. For now I just change DB directly

    if it's necessary, it's possible to write some retry logic, confirmation logic etc.

    :param status: new status of a task
    :param id_: inner checker identifier
    :return: None
    """
    Solution.objects.filter(checker_identifier=id_).update(status=status)
