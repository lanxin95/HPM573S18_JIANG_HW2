# Multi-Attribute Health Status Classification System: Health Utilities Index Mark 3 (HUI3)
# Problem 1: Implement the HUI3 instrument .
# The user will specify the level of 8 attributes in HUI3 instrument and gets the corresponding health score.
C1 = 1.371
C2 = 0.371

MultCoefficients = {'Vision':	    [1, 0.98, 0.89, 0.84, 0.75,	0.61],
                    'Hearing':	    [1, 0.95, 0.89, 0.80, 0.74,	0.61],
                    'Speech':	    [1,	0.94, 0.89,	0.81, 0.68],
                    'Ambulation':   [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':    [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':	    [1,	0.95, 0.85, 0.64, 0.46],
                    'Cognition':    [1, 0.92, 0.95, 0.83, 0.60, 0.42],
                    'Pain':	        [1,	0.96, 0.90,	0.77, 0.55]}


def get_score(Vision, Hearing, Speech, Ambulation, Dexterity, Emotion, Cognition, Pain):
    """
    :param Vision
    :param Hearing
    :param Speech
    :param Ambulation
    :param Dexterity
    :param Emotion
    :param Cognition
    :param Pain
    :return: Score: utility score of chronic health status where dead has a utility of 0.00 and healthy has a utility of 1.00.
    """

    # ensure the entered health dimension levels are acceptable
    if not (Vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision level can take only 1, 2, 3, 4, 5 or 6')
    if not (Hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing level can take only 1, 2, 3, 4, 5 or 6')
    if not (Speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech level can take only 1, 2, 3, 4 or 5')
    if not (Ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation level can take only 1, 2, 3, 4, 5 or 6')
    if not (Dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity level can take only 1, 2, 3, 4, 5 or 6')
    if not (Emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion level can take only 1, 2, 3, 4 or 5')
    if not (Cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition level can take only 1, 2, 3, 4, 5 or 6')
    if not (Pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain level can take only 1, 2, 3, 4, 5')
    #u* = 1.371 (b1 * b2 * b3 * b4 * b5 * b6 * b7 * b8) - 0.371
    print("HUI3 Multi-Attribute Utility Function")
    score = C1
    score *= MultCoefficients['Vision'][Vision - 1]
    score *= MultCoefficients['Hearing'][Hearing - 1]
    score *= MultCoefficients['Speech'][Speech - 1]
    score *= MultCoefficients['Ambulation'][Ambulation - 1]
    score *= MultCoefficients['Dexterity'][Dexterity - 1]
    score *= MultCoefficients['Emotion'][Emotion - 1]
    score *= MultCoefficients['Cognition'][Cognition - 1]
    score *= MultCoefficients['Pain'][Pain - 1]
    score -= C2
    return score



