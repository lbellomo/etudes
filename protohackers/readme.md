# protohackers

## testing the solution

The solutions use the fly.io free tier and that is why they are dockerized.

To deploy:
```
flyctl deploy
```

To look at the ip:
```
flyctl info
```


Finally to delete them:
```
# check the app name 
flyctl list apps

# delete de app
flyctl destroy the-problem-app-name-123
```
