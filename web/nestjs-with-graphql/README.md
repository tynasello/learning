Two NestJS-GraphQL (Code First) APIs with CRUD commands to Sqlite database.

libary-api 
- Prisma ORM
- Implements user model with protected routes using JWT authentication 
  - Custom guards enabling passport-jwt strategy
  - Access and refresh tokens
  - Bcrypt to hash and compare passwords and tokens
  
movie-api
- TypeORM ORM
  

<hr >

Library-api
```
├── nest-cli.json
├── package-lock.json
├── package.json
├── prisma
│   ├── dev.db
│   ├── migrations
│   │   ├── 20220215213918_init
│   │   │   └── migration.sql
│   │   ├── 20220216151952_add_user
│   │   │   └── migration.sql
│   │   └── migration_lock.toml
│   └── schema.prisma
├── src
│   ├── app.controller.ts
│   ├── app.module.ts
│   ├── app.service.ts
│   ├── auth
│   │   ├── auth.module.ts
│   │   ├── auth.resolver.ts
│   │   ├── auth.service.ts
│   │   └── dto
│   │       ├── login-signup-refresh-response.ts
│   │       ├── login.input.ts
│   │       └── logout.response.ts
│   ├── authors
│   │   ├── authors.module.ts
│   │   ├── authors.resolver.ts
│   │   ├── authors.service.ts
│   │   ├── dto
│   │   │   ├── create-author.input.ts
│   │   │   └── update-author.input.ts
│   │   └── entities
│   │       └── author.entity.ts
│   ├── books
│   │   ├── books.module.ts
│   │   ├── books.resolver.ts
│   │   ├── books.service.ts
│   │   ├── dto
│   │   │   ├── create-book.input.ts
│   │   │   └── update-book.input.ts
│   │   └── entities
│   │       └── book.entity.ts
│   ├── common
│   │   ├── guards
│   │   │   ├── index.ts
│   │   │   ├── jwt-auth.guard.ts
│   │   │   └── jwt-refresh-auth.guard.ts
│   │   └── strategies
│   │       ├── at.strategy.ts
│   │       ├── index.ts
│   │       └── rt.strategy.ts
│   ├── main.ts
│   ├── prisma.service.ts
│   ├── schema.gql
│   ├── types
│   │   ├── index.ts
│   │   └── tokent.type.ts
│   └── users
│       ├── dto
│       │   ├── create-user.input.ts
│       │   └── update-user.input.ts
│       ├── entities
│       │   └── user.entity.ts
│       ├── users.module.ts
│       ├── users.resolver.ts
│       └── users.service.ts
├── test
│   ├── app.e2e-spec.ts
│   └── jest-e2e.json
├── tsconfig.build.json
└── tsconfig.json
```

Movie-api
```
├── nest-cli.json
├── package-lock.json
├── package.json
├── src
│   ├── actor
│   │   ├── actor.module.ts
│   │   ├── actor.resolver.ts
│   │   ├── actor.service.ts
│   │   ├── dto
│   │   │   ├── create-actor.input.ts
│   │   │   └── update-actor.input.ts
│   │   └── entities
│   │       └── actor.entity.ts
│   ├── app.controller.ts
│   ├── app.module.ts
│   ├── app.service.ts
│   ├── main.ts
│   ├── movies
│   │   ├── dto
│   │   │   └── create-movie.input.ts
│   │   ├── entities
│   │   │   └── movie.entity.ts
│   │   ├── movies.module.ts
│   │   ├── movies.resolver.ts
│   │   └── movies.service.ts
│   └── schema.gql
├── test
│   ├── app.e2e-spec.ts
│   └── jest-e2e.json
├── tsconfig.build.json
└── tsconfig.json
```