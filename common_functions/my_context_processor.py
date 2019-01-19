def get_session_username(request):
    '''
    在本工程中，很多view函数需要用到session_username变量，为不
    重复工作，写一个上下文处理器。
    ''' 
    session_username = request.session.get('session_username')
    return {'session_username':session_username}
