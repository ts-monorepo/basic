# Basic TypeScript monorepo

- ✅ typescript
- ✅ turborepo
- ✅ pnpm

### How to use

```zsh
git clone https://github.com/ts-monorepo/basic.git basic-monorepo
cd basic-monorepo
pnpm install
pnpm start-prepare # install git hooks
```

```zsh
pnpm dev
```

```zsh
pnpm test
```

```zsh
pnpm build
```

### Structure

apps:

- `apps/hello` Simple TypeScript hello program
- `apps/py-hello` Simple Python Flask hello program

Common config packages:

- `config/ts-config`
- `config/eslint-config`
- `config/test-config` for pure TS testing, support decorators
- `config/vitest-config` for react.js testing

### TODOs

- [ ] Make it easy to sync the template
