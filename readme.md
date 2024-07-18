# World Cup Football Tournament System

This project is a simulation of the FIFA World Cup tournament system using Object-Oriented Programming (OOP) principles. It allows users to manage teams, groups, and stages of the tournament up to the final match.

## Project Structure

The project consists of the following components/classes:

- **Team Class**: Represents a football team with attributes like country, results, etc.
- **Group Class**: Manages a group of teams within the tournament.
- **Round16 Class**: Handles the round of 16 matches and results.
- **QuarterFinal Class**: Manages the quarter-final matches and results.
- **SemiFinal Class**: Handles the semi-final matches and results.
- **Final Class**: Manages the final match and determines the tournament winner.

## Functionality

- **Adding Teams**: Users can add 32 teams and assign them to 8 groups.
- **Progression**: Winners from each group move to the round of 16, then to the quarter-finals, semi-finals, and finally the final.
- **Match Results**: Users input match results which determine the progression of teams through the tournament stages.
- **Display**: The system prints results for each stage of the tournament.
- **Winner Determination**: The system identifies and displays the winner of the World Cup.

## Usage

1.  **Initialization**: Create instances of the Team class for each of the 32 teams.
2.  **Group Allocation**: Assign teams to instances of the Group class to form 8 groups.
3.  **Progression**: Automatically move winning teams from groups to subsequent stages (Round16, QuarterFinal, SemiFinal, Final).
4.  **Input Results**: Enter match results to progress through each stage.
5.  **Output**: View results for each stage until the winner is determined.

## Testing

- **World Cup 2022**: Test the system using the matches and results from the 2022 FIFA World Cup.
- **Custom Tests**: Verify system functionality with different teams and random results.

## GUI System

Implement of a Graphical User Interface (GUI) that allows:

- Entering team data.
- Inputting match results.
- Viewing results for each stage.
- Designing the GUI with buttons, fields, flags images, and multiple windows.

## Contributors

- **Taha Al-Hadhary**

## License

This project is licensed under the MIT License - see the LICENSE file for details.
