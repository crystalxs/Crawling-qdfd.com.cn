# crawling-qdfd.com.cn

## Setting under Win

1. Start -> All Programs -> Accessoriest -> System Tools -> Task Scheduler  
2. Action -> Create Task  
  + Add a task name, (description, security options) under General tab.  
  + Add a new trigger under Triggers tab:  
      + Set as daily, on 6:00:00 PM on +8:00 time zone.
  + Add a new action under Actions tab: 
      + Set action as `Start a program`;  
      + add `test.bat` to Program/script.
