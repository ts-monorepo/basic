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

- `apps/hello`

Common config packages:

- `config/ts-config`
- `config/eslint-config`
- `config/test-config`

### TODOs

- [ ] Make it easy to sync the template
