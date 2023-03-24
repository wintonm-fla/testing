from prefect import flow, task

@flow
def test():
    print('hello')