---
categories:
  - "[[Clippings]]"
title: "After Refactoring 20 Spring Boot Projects, This Architecture Made My Codebase Stable and Maintainable"
source: "https://medium.com/@umeshcapg/after-refactoring-20-spring-boot-projects-this-architecture-made-my-codebase-stable-and-e0b36e8b8153"
author:
  - "[[Umesh Kumar Yadav]]"
published: 2026-08-14
created: 2026-08-18
description: "You're reading for free via Umesh Kumar Yadav's Friend Link."
tags:
  - "clippings"
url: "https://medium.com/@umeshcapg/after-refactoring-20-spring-boot-projects-this-architecture-made-my-codebase-stable-and-e0b36e8b8153"
---
*How modular design, clear transaction boundaries, centralized exception handling, and event-driven architecture can keep a Spring Boot application maintainable as the business grows.*

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*7KCZtX5GEFV79pC4O9OQvQ.png)

AI image

[**Please find friend link here.**](https://medium.com/@umeshcapg/after-refactoring-20-spring-boot-projects-this-architecture-made-my-codebase-stable-and-e0b36e8b8153?sk=11f2ec399e94bc94b6e9d58301454505)

A Spring Boot project often starts beautifully.

You have a few controllers, a few services, some repositories, and everything seems easy to understand.

Then the business grows.

New features are added. More integrations appear. More developers join the team. What was once a clean codebase gradually becomes a collection of giant services, duplicated logic, inconsistent error handling, and tightly coupled modules.

Eventually, a simple change can require hours of investigation.

The problem is often not Spring Boot itself.

It is **architecture**.

After refactoring multiple Spring Boot projects, one lesson becomes increasingly clear:

> *A good architecture is not about creating more layers. It is about creating clear boundaries.*

This article presents a practical architecture for keeping Spring Boot applications modular…

## 1\. The Two Problems I See Again and Again

Before discussing the solution, let’s look at two common situations.

## The “God Service”

Imagine opening:

```c
OrderService.java
```

and discovering that it contains thousands of lines.

It handles:

- Order creation
- Order status changes
- Payment processing
- User points
- Notifications
- Report generation
- Inventory operations

Now someone asks:

> *“Can you make a small change to order status?”*

You cannot simply change one method.

First, you need to understand what else the service is doing.

This is a classic **high-coupling / low-cohesion** problem.

## The Exception Handling Problem

Another common situation is inconsistent error handling.

For example:

```c
try {
    paymentService.pay(request);
} catch (Exception e) {
    return "PAYMENT_FAILED";
}
```

Meanwhile, another service simply does:

```c
throw new BusinessException("Order not found");
```

And another layer catches the exception and logs it.

The result?

There is no consistent contract for:

- Error responses
- HTTP status codes
- Logging
- Business exceptions
- Validation failures

The source material highlights exactly this kind of inconsistency as a major troubleshooting problem.

The solution is to establish architectural standards early.

## 2\. Organize the Project Around Business Modules

A common Spring Boot project starts with a technical-layer structure:

```c
controller/
service/
repository/
entity/
dto/
```

This looks clean initially.

But as the application grows, these directories can become enormous.

Instead, organize the application primarily around **business modules**.

For example:

```c
src/main/java
└── com/example/project
    ├── common
    │   ├── annotation
    │   ├── config
    │   ├── constant
    │   ├── exception
    │   ├── utils
    │   └── vo
    │
    ├── order
    │   ├── controller
    │   ├── service
    │   ├── dao
    │   ├── entity
    │   ├── dto
    │   └── vo
    │
    ├── user
    │   ├── controller
    │   ├── service
    │   ├── dao
    │   ├── entity
    │   ├── dto
    │   └── vo
    │
    └── ProjectApplication.java
```

The important idea is:

**Business boundaries come first.**

Inside each business module, technical responsibilities can then be separated.

The source architecture follows this approach because each module becomes more self-contained, while controller, service, and DAO responsibilities remain explicit.

## 3\. What Each Layer Should Actually Do

A layered architecture only works if the layers have clear responsibilities.

## Controller

The controller should handle HTTP concerns:

- Request mapping
- Input validation
- Authentication-related request information
- Response conversion

It should not contain business rules.

Bad:

```c
@PostMapping("/orders")
public Order createOrder(OrderRequest request) {

    if (request.getItems().isEmpty()) {
        throw new RuntimeException("No items");
    }
    // 100 lines of business logic...
    return orderRepository.save(order);
}
```

Better:

```c
@PostMapping("/orders")
public Result<OrderVO> createOrder(
        @Valid @RequestBody OrderRequest request) {

    Order order = orderService.createOrder(request);
    return Result.success(convertToVO(order));
}
```

The controller coordinates the request.

The service owns the business operation.

## Service

The service should contain business use cases.

For example:

```c
@Service
@RequiredArgsConstructor
public class OrderService {

    private final OrderRepository orderRepository;

    @Transactional
    public Order createOrder(OrderRequest request) {
        // business operation
    }
}
```

Avoid turning one service into the dumping ground for every operation related to an entity.

Instead, when necessary, split large business operations into focused services:

```c
UserRegistrationService
UserLoginService
UserProfileService
UserQueryService
```

This improves cohesion and testability.

## DAO / Repository

The data-access layer should focus on persistence.

For example:

```c
public interface OrderRepository
        extends JpaRepository<Order, Long> {

    Optional<Order> findByOrderNumber(String orderNumber);
}
```

Business decisions should not be buried inside repository implementations.

## 4\. Standardize API Responses

A mature backend should have a predictable API contract.

One approach is a generic response wrapper:

```c
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Result<T> {

    private Integer code;
    private String message;
    private T data;
    public static <T> Result<T> success() {
        return new Result<>(200, "Operation successful", null);
    }
    public static <T> Result<T> success(T data) {
        return new Result<>(200, "Operation successful", data);
    }
    public static <T> Result<T> error(String message) {
        return new Result<>(500, message, null);
    }
    public static <T> Result<T> error(
            Integer code,
            String message) {
        return new Result<>(code, message, null);
    }
}
```

A successful response might look like:

```c
{
  "code": 200,
  "message": "Operation successful",
  "data": {
    "id": 1,
    "name": "Example"
  }
}
```

The benefit is consistency.

Clients do not have to learn a completely different response format for every endpoint.

## A practical caveat

In a modern REST API, you do not necessarily need to wrap every response in a custom `Result<T>`.

HTTP already provides status semantics.

For example:

```c
200 OK
201 Created
400 Bad Request
404 Not Found
409 Conflict
500 Internal Server Error
```

The important architectural principle is **consistency**, not the wrapper itself.

## 5\. Stop Putting try-catch Everywhere

One of the biggest improvements you can make is centralized exception handling.

Instead of:

```c
public User getUser(Long id) {

    try {
        return repository.findById(id)
                .orElseThrow(...);
    } catch (Exception e) {
        log.error("Something failed", e);
        throw e;
    }
}
```

Use Spring’s global exception handling:

```c
@RestControllerAdvice
@Slf4j
public class GlobalExceptionHandler {

@ExceptionHandler(BusinessException.class)
    public Result<?> handleBusinessException(
            BusinessException e) {
        log.warn("Business error: {}", e.getMessage());
        return Result.error(
                e.getCode(),
                e.getMessage()
        );
    }
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public Result<?> handleValidationException(
            MethodArgumentNotValidException e) {
        String message = e.getBindingResult()
                .getFieldError()
                .getDefaultMessage();
        return Result.error(400, message);
    }
    @ExceptionHandler(Exception.class)
    public Result<?> handleException(Exception e) {
        log.error("Unexpected system error", e);
        return Result.error(
                500,
                "Something went wrong. Please try again later."
        );
    }
}
```

Now your business code can concentrate on the happy path.

Benefits include:

- Cleaner services
- Consistent error responses
- Centralized logging
- Easier troubleshooting
- Easier modification of error policies

This centralized approach is one of the core recommendations in the source material.

## 6\. Configuration Should Not Be Scattered Everywhere

Configuration is another area that becomes painful as applications grow.

A reasonable structure is:

```c
application.yml
application-dev.yml
application-test.yml
application-prod.yml
```

Common configuration belongs in the base configuration.

Environment-specific values belong in environment-specific configuration.

More importantly:

**Do not commit secrets into Git.**

Avoid:

```c
spring:
  datasource:
    password: my-super-secret-password
```

Prefer:

```c
spring:
  datasource:
    password: ${DB_PASSWORD}
```

Then provide the value through your deployment environment or secret-management system.

## Use @ConfigurationProperties

Instead of scattering:

```c
@Value("${app.jwt.secret}")
private String secret;
```
```c
@Value("${app.jwt.expiration}")
private long expiration;
```

group related configuration:

```c
@Component
@ConfigurationProperties(prefix = "app.jwt")
@Data
public class JwtProperties {

    private String secret;
    private long expiration;
    private String header;
}
```

Configuration becomes:

```c
app:
  jwt:
    secret: ${JWT_SECRET}
    expiration: 3600
    header: Authorization
```

This gives you:

- Type-safe configuration
- Centralized configuration
- IDE support
- Better maintainability
- Clear separation between configuration and business logic

These are the same configuration-management principles emphasized in the source material.

## 7\. Transactions: The Most Common Architectural Trap

Adding:

```c
@Transactional
```

does not automatically make your architecture correct.

The important question is:

> ***What should actually be inside the transaction?***

A transaction should normally be:

- Small
- Focused
- Database-oriented
- Easy to complete quickly

Avoid long-running remote calls inside a database transaction.

For example, this looks attractive:

```c
@Transactional
public Order createOrder(OrderRequest request) {

    Order order = orderRepository.save(...);
    inventoryService.decrease(request.getItems());
    paymentService.charge(request.getPayment());
    notificationService.send(...);
    return order;
}
```

But now the database transaction potentially remains open while:

- Inventory service responds
- Payment gateway responds
- Notification service responds

If one remote service becomes slow, your database transaction remains open.

That can increase lock duration and reduce throughput.

The source material explicitly identifies remote calls inside transactions as a flaw and recommends decoupling them.

## 8\. Think in Terms of Transaction Boundaries

A better design is:

```c
Create Order
     |
     v
Database Transaction
     |
     v
Order CREATED
     |
     v
Publish Event
     |
     v
Inventory Processing
     |
     v
Success / Failure
```

The database transaction handles the local state transition.

The asynchronous workflow handles the distributed operation.

For example:

```c
@Service
@RequiredArgsConstructor
public class OrderService {

    private final OrderRepository orderRepository;
    private final ApplicationEventPublisher eventPublisher;

    @Transactional
    public Order createOrder(OrderRequest request) {
        Order order = new Order();
        order.setStatus(OrderStatus.CREATED);
        order.setItems(request.getItems());
        order.setTotalAmount(
                calculateTotal(request.getItems())
        );
        Order savedOrder = orderRepository.save(order);
        eventPublisher.publishEvent(
                new OrderCreatedEvent(
                        savedOrder.getId(),
                        request.getItems()
                )
        );
        return savedOrder;
    }
}
```

However, there is an important subtlety.

If the event must only be processed **after the transaction successfully commits**, use transaction-aware event handling.

For example:

```c
@Component
@RequiredArgsConstructor
public class InventoryEventListener {

    private final InventoryService inventoryService;

    @Async
    @TransactionalEventListener(
            phase = TransactionPhase.AFTER_COMMIT
    )
    public void handleOrderCreated(
            OrderCreatedEvent event) {
        inventoryService.decrease(
                event.getItems()
        );
    }
}
```

Now the inventory operation is decoupled from the original database transaction.

## 9\. Eventual Consistency Is Sometimes the Right Answer

When multiple services participate in a workflow, trying to maintain one giant ACID transaction across all of them can make the system fragile.

Instead, consider:

```c
Order Service
     |
     | OrderCreated
     v
Message Broker
     |
     +------> Inventory Service
     |
     +------> Notification Service
     |
     +------> Analytics Service
```

Each consumer can process the event independently.

If inventory temporarily fails, you can retry.

If notification fails, you can retry notification without rolling back the order itself.

This introduces **eventual consistency**, but that is often a better trade-off for distributed systems.

The source material recommends compensation and eventual consistency when operations cross service boundaries.

## 10\. Retries Need More Than a while Loop

Distributed systems fail.

A remote service may:

- Timeout
- Return 500
- Become temporarily unavailable
- Process the request but lose the response
- Recover after several seconds

Therefore, asynchronous processing should usually have:

```c
Retry
  |
  +--> Retry succeeds
  |
  +--> Retry fails
          |
          v
      Dead Letter / Manual Review
```

A practical retry mechanism should consider:

- Maximum retry count
- Exponential backoff
- Idempotency
- Duplicate-event handling
- Dead-letter queues
- Alerting
- Compensation

The source example uses an event log to prevent duplicate processing and a retry queue when inventory processing fails.

## 11\. Idempotency Is Critical

Suppose this event is delivered twice:

```c
OrderCreated(orderId=1001)
OrderCreated(orderId=1001)
```

If your inventory service blindly deducts stock twice, you have a serious consistency problem.

Therefore, consumers should be designed to be **idempotent**.

For example:

```c
if (eventLogService.isEventProcessed(event.getOrderId())) {
    return;
}
```

Then process the event and record the result.

In production systems, you should make this stronger with an appropriate persistence-level uniqueness constraint or idempotency key rather than relying only on an in-memory check.

## 12\. Before and After: Refactoring a Giant UserService

Consider a typical legacy service:

```c
@Service
public class UserService {

    public User register(UserRegisterDTO dto) {
        // validation
        // save user
        // send email
        // send SMS
        // logging
        // more business logic
    }
    // Login
    // Password reset
    // Profile update
    // User query
    // 2,000+ more lines...
}
```

The class has become a **God object**.

The problem isn’t that `UserService` exists.

The problem is that it owns too many responsibilities.

## 13\. Split the Use Cases

A cleaner design could look like:

```c
UserController
      |
      +----> UserRegisterService
      |
      +----> UserLoginService
      |
      +----> UserProfileService
      |
      +----> UserQueryService
```

For example:

```c
@RestController
@RequestMapping("/users")
@RequiredArgsConstructor
public class UserController {

    private final UserRegisterService userRegisterService;
    private final UserQueryService userQueryService;

    @PostMapping("/register")
    public Result<UserVO> register(
            @Valid @RequestBody UserRegisterDTO dto) {
        User user = userRegisterService.register(dto);
        return Result.success(convertToVO(user));
    }
    @GetMapping("/{id}")
    public Result<UserDetailVO> getById(
            @PathVariable Long id) {
        UserDetail detail =
                userQueryService.getUserDetail(id);
        return Result.success(
                convertToDetailVO(detail)
        );
    }
}
```

Now registration and querying have separate boundaries.

## 14\. Make Registration Its Own Business Operation

```c
@Service
@RequiredArgsConstructor
@Transactional(rollbackFor = Exception.class)
public class UserRegisterService {

private final UserRepository userRepository;
    private final UserValidator userValidator;
    private final PasswordEncoder passwordEncoder;
    private final UserEventPublisher eventPublisher;
    public User register(UserRegisterDTO dto) {
        userValidator.validateRegistration(dto);
        User user = createUserFromDto(dto);
        User savedUser = userRepository.save(user);
        eventPublisher.publishUserRegisteredEvent(
                savedUser
        );
        return savedUser;
    }
    private User createUserFromDto(
            UserRegisterDTO dto) {
        User user = new User();
        user.setUsername(dto.getUsername());
        user.setPassword(
                passwordEncoder.encode(dto.getPassword())
        );
        user.setEmail(dto.getEmail());
        user.setPhone(dto.getPhone());
        user.setCreateTime(new Date());
        return user;
    }
}
```

Notice what is **not** here.

There is no:

```c
emailService.send(...)
smsService.send(...)
```

The core registration use case does not need to know how welcome notifications work.

## 15\. Decouple Notifications with Events

Create an event:

```c
public record UserRegisteredEvent(
        Long userId,
        String email,
        String phone
) {}
```

Publish it:

```c
@Component
@RequiredArgsConstructor
public class UserEventPublisher {

private final ApplicationEventPublisher eventPublisher;
    public void publishUserRegisteredEvent(User user) {
        eventPublisher.publishEvent(
                new UserRegisteredEvent(
                        user.getId(),
                        user.getEmail(),
                        user.getPhone()
                )
        );
    }
}
```

Then process it separately:

```c
@Component
@RequiredArgsConstructor
public class UserRegistrationListener {

private final EmailService emailService;
    private final SmsService smsService;
    @Async
    @EventListener
    public void handleUserRegistered(
            UserRegisteredEvent event) {
        try {
            emailService.sendWelcomeEmail(
                    event.email()
            );
        } catch (Exception e) {
            log.error(
                    "Welcome email failed for user {}",
                    event.userId(),
                    e
            );
        }
        try {
            smsService.sendWelcomeSms(
                    event.phone()
            );
        } catch (Exception e) {
            log.error(
                    "Welcome SMS failed for user {}",
                    event.userId(),
                    e
            );
        }
    }
}
```

Now the registration flow is independent of the notification implementation.

The source material identifies the resulting benefits as clearer responsibilities, better transaction boundaries, decoupled notifications, higher testability, and centralized exception handling.

## 16\. But Be Careful with @Async and Events

There is an important production consideration here.

An in-process Spring event is **not automatically a durable message**.

If your application crashes before an asynchronous listener processes the event, the event may be lost.

For non-critical operations such as:

- Metrics
- Some notifications
- Internal cache refreshes

this may be acceptable.

For critical workflows such as:

- Payment
- Inventory
- Order fulfillment
- Financial transactions

consider a durable messaging solution and patterns such as:

- Transactional Outbox
- Kafka
- RabbitMQ
- RocketMQ
- Dead-letter queues
- Idempotent consumers

The architectural principle is more important than the specific broker:

> *The database transaction and distributed message delivery should be designed as two related but distinct concerns.*

## 17\. High Cohesion, Low Coupling

Two architectural principles repeatedly show up in good systems.

## High Cohesion

Related responsibilities should stay together.

For example:

```c
UserRegistrationService
```

should contain logic primarily related to registration.

Not:

```c
UserRegistrationService
    + PDF generation
    + Email delivery
    + Inventory
    + Analytics
    + Report generation
```

## Low Coupling

Components should have minimal unnecessary dependencies.

Instead of:

```c
public class OrderService {

    private MysqlOrderRepository repository;
}
```

prefer:

```c
public class OrderService {

    private final OrderRepository repository;
}
```

The service depends on an abstraction.

The source material identifies high cohesion, low coupling, separation of concerns, and dependency inversion as core architectural principles.

## 18\. Don’t Refactor Everything at Once

One of the biggest mistakes during refactoring is deciding:

> *“This architecture is bad. Let’s rewrite the whole application.”*

That is often riskier than the original problem.

Instead, use **incremental refactoring**.

When you touch an existing feature:

```c
Old code
   |
   v
Understand behavior
   |
   v
Add tests
   |
   v
Extract responsibility
   |
   v
Improve boundaries
   |
   v
Deploy
```

Then repeat.

The source material recommends improving the surrounding structure while modifying code, performing regular reviews, and relying on automated tests to make refactoring safer.

## 19\. A Practical Architecture Checklist

When reviewing a Spring Boot project, ask:

## Project structure

- Is the code organized around business modules?
- Can I find everything related to a business capability easily?
- Are common utilities genuinely common?

## Controllers

- Are controllers thin?
- Are business rules outside controllers?
- Is request validation standardized?

## Services

- Does each service have a focused responsibility?
- Are there giant `*Service` classes?
- Are use cases clearly separated?

## Persistence

- Are repositories responsible primarily for data access?
- Are business rules leaking into the persistence layer?

## Exceptions

- Is exception handling centralized?
- Are business exceptions standardized?
- Are unexpected exceptions logged with sufficient context?

## Configuration

- Are environment-specific settings separated?
- Are secrets externalized?
- Are related settings grouped with `@ConfigurationProperties`?

## Transactions

- Are transaction boundaries clear?
- Are transactions unnecessarily large?
- Are remote calls happening inside database transactions?

## Distributed workflows

- Are asynchronous operations durable when they need to be?
- Are consumers idempotent?
- Is retry behavior defined?
- Is there a dead-letter or compensation strategy?

## Testing

- Can individual business services be unit tested?
- Does changing one module require changing unrelated tests?
- Are architectural boundaries protected by tests?

## 20\. The Architecture I Would Aim For

A mature Spring Boot application can evolve toward something like:

```c
┌──────────────────────┐
          │      Controller      │
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │   Application/       │
          │   Use Case Service   │
          └──────────┬───────────┘
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
┌────────────┐ ┌────────────┐ ┌────────────┐
│ Domain     │ │ Repository │ │   Events   │
│ Logic      │ │            │ │            │
└────────────┘ └─────┬──────┘ └─────┬──────┘
                      │              │
                      ▼              ▼
                 ┌─────────┐    ┌───────────┐
                 │Database │    │ Message   │
                 │         │    │  Broker   │
                 └─────────┘    └─────┬─────┘
                                      │
                 ┌────────────────────┼─────────────────┐
                 ▼                    ▼                 ▼
            Inventory            Notification       Analytics
```

The exact architecture will vary by system.

A small CRUD application does not need Kafka, complex event orchestration, or dozens of abstractions.

Architecture should follow **complexity**, not fashion.

## 21\. Final Takeaway

A maintainable Spring Boot application is not created by adding more packages.

It is created by establishing **boundaries**.

The most important principles are:

1. **Organize around business modules**, not only technical layers.
2. **Keep controllers thin** and business logic in focused services.
3. **Avoid God services** by splitting large use cases.
4. **Standardize API and exception handling.**
5. **Externalize configuration and secrets.**
6. **Keep transactions small and focused.**
7. **Avoid remote calls inside database transactions.**
8. **Use events and messaging to decouple distributed workflows.**
9. **Design asynchronous consumers for idempotency and retries.**
10. **Refactor incrementally instead of waiting for the codebase to become unmaintainable.**

The real goal of architecture is not to make the project look sophisticated.

It is to make the next change **cheaper, safer, and easier to understand**.

When a developer can modify one business capability without needing to understand half of the application, you know the architecture is doing its job.

And that, ultimately, is what good Spring Boot architecture should achieve.

Thank you for reading!

If you found this article useful, feel free to give it a clap 👏, share it with your friends, and follow for more deep dives into distributed systems, Spring Boot architecture, Kafka, Redis, and high-scale backend engineering.

😊 Your support is the biggest motivation to continue sharing technical insights