# Async python queue feed, with synchronized access

A python implementation for a multithreaded file accessor,
generating numpy arrays, and then feeding it into a queue, which has synchronized access

### What is the goal

Goal of this is the feasibility for an async feed / sync read within certain parameters

### Generator

- Data for this is generated via the `generator.py` script, which will create files to test reading np arrays
- Data is stored in the `data` directory