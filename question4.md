## Diagrama de Relacionamentos

```plaintext
+------------------+          +--------------+          +----------------+ 
|    Clientes      |          |    Estados   |          |  TiposTelefone  | 
+------------------+          +--------------+          +----------------+ 
| id_cliente (PK)  |<-------->| id_estado (PK)           | id_tipo_telefone (PK)|
| razao_social     |          | nome_estado              | tipo_telefone       |
| id_estado (FK)   |          +--------------+          +----------------+ 
+------------------+                  
          |                                           
          |                                           
          |                                           
+------------------+                                    
|    Telefones     |                                    
+------------------+                                    
| id_telefone (PK) |                                    
| numero_telefone  |                                    
| id_cliente (FK)  |                                    
| id_tipo_telefone (FK)                               
+------------------+         
```

SELECT c.id_cliente, c.razao_social, t.numero_telefone
FROM Clientes c
JOIN Estados e ON c.id_estado = e.id_estado
JOIN Telefones t ON c.id_cliente = t.id_cliente
WHERE e.id_estado = 'SP';

