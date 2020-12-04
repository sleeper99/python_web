## FIND_IN_SET()

* syntax

  FIND_IN_SET(search string, string list)

* advantage

  faster than `LIKE` or `LOCATE`

## concurrent.futures

* When using multi-task execute transition sql, **process** is the way to go, cuz **thread** will share resource and make the transition can't commit

  ```python
  # some example
  import concurrent.futures
  
  def insert_data():
      transition.begin()
      execute(sql)
      transition.commit()
  
  with concurrent.futures.ProcessPoolExecutor() as executor:
      executor.summit(insert_data)
  ```

## INSER ON DUPLICATE KEY UPDATE

* pk or unique

  ```python
  def insert_on_duplicate_key_update(self, data, transition=False) -> None:
          """
          base on pk or unique key to insert or update
          :param data: date to insert
          :param transition: begin tansition
          :return:
          """
          columns = ','.join(data)
          values = ':' + ',:'.join(data)
          update_values = ','.join([key + '=:' + key for key in data])
          sql = """INSERT INTO {0}({1}) VALUES({2})
              ON DUPLICATE KEY UPDATE {3}""".format(self.service.model.__tablename__, columns, values, update_values)
  
          try:
              self.service.session.execute(sql, data)
          except Exception as e:
              self.rollback()
              raise e
  
          if not transition:
              self.commit()
  ```

* other contidion

  ```python
  def insert_if_not_exists(self, data, conditions, transition=False) -> None:
          data.update(conditions)
          columns = ','.join(data)
          values = ':' + ',:'.join(data)
          where = ' AND '.join([key + '=:' + key for key in conditions])
          sql = """INSERT INTO {0}({1})
              SELECT {2} WHERE NOT EXISTS
              (SELECT * FROM {0} WHERE {3})""".format(self.service.model.__tablename__, columns, values, where)
  
          try:
              self.service.session.execute(sql, data)
          except Exception as e:
              self.rollback()
              raise e
  
          if not transition:
              self.commit()
  ```

## check transations
```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_TRX;
```
  
