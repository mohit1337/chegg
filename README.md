# chegg
Automation over chegg expert QnA

# Workflow
1. Login to chegg and start loading questions
2. If len(text) on question > 1000: skip question
3. If any keyword found from `ignore_words`: skip question
4. If any keyword found from `fav_words`: retain question
5. If a matching question is found, notify on pushbullet with question text/image
6. Pushbullet workflow can also skip a question
