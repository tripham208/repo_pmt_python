| Feature      | Function                                                                   | Generator                                                                              |
|--------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Value        | Returns all values at once                                                 | Yields values one at a time, on demand                                                 |
| Execution    | Executes **completely before returning**                                   | **Pauses after yielding**, resumes when next value is requested                        |
| Keyword      | return                                                                     | yield                                                                                  |
| Memory Usage | Potentially **high**, stores entire sequence in memory                     | **Low**, stores only current value and state for next                                  |
| Iteration    | **Multiple iterations** possible, but requires storing the entire sequence | Designed for **single-pass iteration**, more efficient for large or infinite sequences |

