import random
import time

from celery.task import task

from apps.core.models import Solution


@task()
def check_solution(solution: str, id_: int):
    time.sleep(random.randint(1, 5))
    status = random.choice(['unevaluated', 'correct', 'wrong'])
    send_solution_callback(status=status, id_=id_)


def send_solution_callback(status: str, id_: int):
    """
    function for sending callback if it's a different service. For now I just change DB directly

    if it's necessary, it's possible to write some retry logic, confirmation logic etc.

    :param status: new status of a task
    :param id_: inner checker identifier
    :return: None
    """
    Solution.objects.filter(checker_identifier=id_).update(status=status)
