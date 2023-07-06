```python
from .db_connection import get_db_connection
from src.models.reaction import LiveReactionSchema

def save_reaction(reaction_data):
    db = get_db_connection()
    reaction = LiveReactionSchema().load(reaction_data)
    db.session.add(reaction)
    db.session.commit()
    return reaction.id

def get_reaction_by_id(reaction_id):
    db = get_db_connection()
    reaction = db.session.query(LiveReactionSchema).get(reaction_id)
    return reaction

def get_reactions_by_user_id(user_id):
    db = get_db_connection()
    reactions = db.session.query(LiveReactionSchema).filter_by(user_id=user_id).all()
    return reactions

def update_reaction(reaction_id, reaction_data):
    db = get_db_connection()
    reaction = db.session.query(LiveReactionSchema).get(reaction_id)
    for key, value in reaction_data.items():
        setattr(reaction, key, value)
    db.session.commit()
    return reaction

def delete_reaction(reaction_id):
    db = get_db_connection()
    reaction = db.session.query(LiveReactionSchema).get(reaction_id)
    db.session.delete(reaction)
    db.session.commit()
    return True
```