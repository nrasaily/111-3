from app.database import get_db

def output_formatter(results):
    out = []
    for task in results:
        res = {
            "id": task[0],
            "name": task[1],
            "summary": task[2],
            "description": task[3],
            "is_done": task[4]
        }
        out.append(res)
    return out


def scan():
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(task_id):
    conn = get_db()
    cursor + conn.execute("SELECT * FROM task WHERE id=?", (task_id, )) # comma
    results = cursor.fetchall()
    if results:
        return out_formatter(results)[0]
    return {}

def insert(task_data):
    task_tuple = (
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description")
    )
    statement = """
        INSERT INTO tasks (
            name,
            summary,
            description 
        ) VALUES (?, ?, ?)
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def update_by_id(task_data, task_id):
    task_tuple = (
         task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done"),
        task_id
        
    )
    statement = """ 
    UPDATE task 
         SET
            name = ?,
            summary = ?,
            description = ? ,
            is_done = ?
    WHERE id = ?
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def delete_by_id(task_data, task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?" (task_id, ))
    conn.commit()
