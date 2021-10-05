
```
docker build . -t yaml-include
docker run --rm -v $(pwd)/examples:/app yaml-include base.yaml result.yml
```
