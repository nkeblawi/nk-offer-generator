from models.models import *
import dspy


class ProblemGenerationSignature(dspy.Signature):
    """Given the occupation, list the top 3 real problems and obstacles that this role could or is currently facing."""

    occupation: str = dspy.InputField()
    problems: list[Problem] = dspy.OutputField()


class SubProblemGenerationSignature(dspy.Signature):
    """Break each problem down into 3 steps that the role would have to do or take to be successful."""

    problem: str = dspy.InputField()
    sub_problems: list[SubProblem] = dspy.OutputField()


class ObjectionGenerationSignature(dspy.Signature):
    """Given the main problem, generate a list of top 3 possible objections that the customer may have for why they think they couldn't solve that problem. Order each objection from most common to least common."""

    problem: str = dspy.InputField()
    objections: list[Objection] = dspy.OutputField()


class ProblemSolvingSignature(dspy.Signature):
    """Write up to 3 single sentences on how a single-person service provider would deliver a one-on-one solution. Each sentence will cover one of the following delivery methods: done with you, done for you, and done by you solutions for the given problem and main objection.

    Example:
    Problem: Buying healthy food, and grocery shopping is hard, confusing, i won't like it. I will suck at it.

    Solution 1: In-person grocery shopping, where I take clients to the store and teach them how to shop
    Solution 2: Personalized grocery list, where I teach them how to make their list
    Solution 3: Full-service shopping, where I buy their food for them. 100 percent done for them.
    Solution 4: In-Person orientation (not at store), where I teach them what to get
    Solution 5: Text support while shopping, where I help them if they get stuck
    Solution 6: Phone call while grocery shopping, where I plan to call when they go shopping to provide direction and support
    """

    problem: str = dspy.InputField()
    objections: str = dspy.InputField()
    solutions: Solution = dspy.OutputField()
