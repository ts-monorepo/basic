# test-config

Usage:

First, add `"@configs/test-config": "workspace:*"` to the `package.json` devDependencies:

```json
{
  "devDependencies": {
    "@configs/test-config": "workspace:*",
    "test": "cross-env NODE_ENV=test TS_CONFIG_PATHS=true ts-mocha -p tsconfig.json ./**/*.test.ts --parallel --timeout 30000"
  }
}
```

And add the below to the scripts

```json
{
  "scripts": {
    "test": "cross-env NODE_ENV=test TS_CONFIG_PATHS=true ts-mocha -p tsconfig.json ./**/*.test.ts --parallel --timeout 30000"
  }
}
```
