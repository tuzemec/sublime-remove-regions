# Description
Removes given regions from the current selection set.
And also the chores from pressing multiple times Ctrl+K,Ctrl+D when we want to exclude something from the selection progress. 

# Examples

### Individual items
So, the following scenario: We've selected all occurancies of the word "span" in the document (Alt+F3 when the cursor is on the word "span") and we want to remove the second and the forth occurance from the selection set. Ctrl+Alt+Shift+F3 (or Selection>Remove regions…>Select) will ask for a comma separated values. And since the iteration is zero-based we have to type in "1,3" and press enter.

### Range
Similar to the individual items removal we can specify range. If we want to remove the first item and then the items from 5 to 9 the input should be "1,4-8".

### Odd and Even
The input also can accept the values "odd" and "even". Hopefully it's self explanatory what it does.

### Again
The Selection>Remove…>Again executes again the last given set for exclusion. It's view based.

And remember - Ctrl+U will undo your last selection change.

# Commands
The following commands are available through the command palette and can be bound to keyboard shortcuts:
* remove_regions
* remove_regions_odd
* remove_regions_even
* remove_regions_again

The default keyboard shortcuts are Ctrl+Alt+Shift+F3 for **remove_regions** and Ctrl+Alt+Shift+F2 for **remove_regions_again**.
