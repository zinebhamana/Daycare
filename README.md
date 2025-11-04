# Garderie SOLID Project

## Introduction
This project manages children, employees, events, and payments in a daycare. 
It follows **SOLID principles** to make the code maintainable, extensible, and modular.

---

## SOLID Principles Applied

### 1. Single Responsibility Principle (SRP)
- `Garderie` manages registration only.
- `EventManager` manages events.
- `HTMLManager` manages HTML generation.
**Problem solved:** Avoided mixing data and presentation logic.

### 2. Open/Closed Principle (OCP)
- `Atelier` can be extended to `Trip`, `Meeting`, `Competition`.
- New subscription types (`Abonnement`, `Donation`) can be added.
**Problem solved:** Can extend functionality without modifying existing classes.

### 3. Liskov Substitution Principle (LSP)
- All subclasses of `Atelier` can replace the base class without breaking the code.
- Example: `display_event_details()` works for `Atelier`, `Trip`, `Meeting`.
**Problem solved:** Safe polymorphism.

### 4. Interface Segregation Principle (ISP)
- Small interfaces: `Payable`, `Organizable`, `Registrable`.
- Classes implement only the methods they need.
**Problem solved:** Avoided "fat" interfaces.

### 5. Dependency Inversion Principle (DIP)
- `Garderie` depends on abstractions: `StorageInterface`, `UIInterface`.
- Concrete implementations (`JSONStorage`, `WebUI`) are injected dynamically.
**Problem solved:** High-level modules decoupled from low-level implementations.

---

## How to Run
```bash
python main.py
