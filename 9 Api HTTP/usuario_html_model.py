from usuario import Usuario


head = """
        <head>
            <title>Usuários</title>
            <style>
                table {
                    border-collapse: collapse;
                }

                td, th {
                        border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
            </style>
        </head>
        """

title = "<h1>Usuários</h1>"

table_head = """
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Senha</th>
                </tr>
            </thead>
            """


def table_row(user: Usuario):
    return f"""
            <tr>
                <td>{user.id}</td>
                <td>{user.nome}</td>
                <td>{user.email}</td>
                <td>{user.get_hash_for_html()}</td>
            </tr>
            """


def table_body(users):
    body = "<tbody>"
    for user in users:
        body = body + table_row(user)
    body = body + "</tbody>"
    return body
