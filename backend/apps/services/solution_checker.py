from apps.solution_checker.process_solution import post_solution


class SolutionCheckerAPI:
    """
    Implements logic on communication with external service - solution checker
    """

    def __init__(self):
        """
        use different custom things here: URLs, certificates, any other params for external API usage
        """

    def submit_solution(self, code: str) -> int:
        """
        submit User's solution for checking
        :param code:
        :return:
        """
        checker_id = post_solution(code)

        return checker_id
