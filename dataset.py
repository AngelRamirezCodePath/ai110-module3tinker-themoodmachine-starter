"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    # slang — clear positive signal, not intensifiers
    "fire",
    "slaps",
    "bussin",
    "lit",
    "goated",
    "hype",
    "valid",
    'sick',
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    # slang — clear negative signal
    "mid",
    "trash",
    "cringe",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "This game was boring at first, then it became exciting",
    "I feel very ill",
    "I feel kinda bad when I am having fun instead of doing homework",
    "I get upset when I don't sleep well",
    "I do not feel tired at all",
    "I find it amazing how boring this task is",
    # slang
    "This assignment is lowkey fire",
    "That exam was so mid I almost fell asleep",
    # emojis — edge case: model currently can't read these, so they score neutral
    "Just got my grades back :)",
    "Missed the bus again :(",
    # sarcasm — hard for rule-based models; human label reflects true intent
    "Oh great, another Monday",
    "I absolutely love waiting in line for an hour",
    # ambiguous / mixed
    "Lowkey stressed but kind of proud of myself",
    "I had a great time but I miss everyone already",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "positive",  # "This game was boring at first, but then it became exciting"
    "negative",  # "I feel very ill"
    "negative",  # "I feel kinda bad when I am having fun instead of doing homework"
    "negative",  # "I get upset when I don't sleep well"
    "positive",  # "I do not feel tired at all"
    "mixed",     # "I find it amazing how boring this task is"
    # slang
    "positive",  # "This assignment is lowkey fire"
    "negative",  # "That exam was so mid I almost fell asleep"
    # emojis — labeled by human intent; model will likely miss these
    "positive",  # "Just got my grades back :)"
    "negative",  # "Missed the bus again :("
    # sarcasm — labeled by true sentiment, not surface words
    "negative",  # "Oh great, another Monday"
    "negative",  # "I absolutely love waiting in line for an hour"
    # ambiguous / mixed
    "mixed",     # "Lowkey stressed but kind of proud of myself"
    "mixed",     # "I had a great time but I miss everyone already"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
