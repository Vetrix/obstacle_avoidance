/*
  SELEKSI CALON KRU PROGRAMMING DAGOZILLA 2018
  Take Home Test
  File name: minesweeper.cpp
  Problem 2.2: MineSweeper
*/
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>

using namespace std;

const int BOMB = -1;
const int PLAYING = 555;
const int WIN = 777;
const int LOSE = 666;

int explored_position;
int numberPositionExploredToWin;

typedef struct Map
{
  int **value;
  bool **explored;
};

bool isValidPosition(int row, int col, int size_map)
{
  return (row >= 0 && row < size_map) && (col >= 0 && col < size_map);
}

void inputFieldAndBomb(int &field_size, int &bomb_qty)
{
  cout << "Input the N (size of the fields): ";
  cin >> field_size;

  cout << "Input the B (quantity of bomb): ";
  cin >> bomb_qty;
}

// What does this function do?
// create bomb in random position in map size
int *generateRandomBombPosition(int map_size, int bomb_qty)
{
  srand(time(NULL));
  int size = map_size * map_size;
  int arr[size];
  for (int i = 0; i < size; i++)
    arr[i] = i;

  int randomMoves = map_size / 2;
  for (int i = 0; i < randomMoves; ++i)
  {
    int j = rand() % size;
    if (j != i)
      std::swap(arr[i], arr[i + j]);
  }
  int *bomb_position = new int[bomb_qty];
  for (int i = 0; i < bomb_qty; i++)
    bomb_position[i] = arr[i];

  return bomb_position;
}

void raiseMapValue(Map &map, int size, int row, int col)
{
  if (isValidPosition(row, col, size) && map.value[row][col] != BOMB)
    map.value[row][col]++;
}

// What does this function do?
// change value around bombs
void raiseMapValueAround(Map &map, int size, int row, int col)
{
  raiseMapValue(map, size, row - 1, col - 1);
  raiseMapValue(map, size, row - 1, col);
  raiseMapValue(map, size, row - 1, col + 1);
  raiseMapValue(map, size, row, col - 1);
  raiseMapValue(map, size, row, col + 1);
  raiseMapValue(map, size, row + 1, col - 1);
  raiseMapValue(map, size, row + 1, col);
  raiseMapValue(map, size, row + 1, col + 1);
}

void initiateMap(Map &map, int size, int bomb_qty)
{
  map.value = new int *[size];
  map.explored = new bool *[size];

  for (int i = 0; i < size; i++)
  {
    map.value[i] = new int[size];
    map.explored[i] = new bool[size];
    for (int j = 0; j < size; j++)
    {
      map.value[i][j] = 0;
      map.explored[i][j] = false;
    }
  }

  int *arr = generateRandomBombPosition(size, bomb_qty);
  int row, col;

  for (int i = 0; i < bomb_qty; i++)
  {
    row = arr[i] / size;
    col = arr[i] % size;
    cout << "Bomb generated at " << row << " " << col << endl;
    raiseMapValueAround(map, size, row, col);
    map.value[row][col] = BOMB;
  }
}

void printMap(Map map, int size)
{
  for (int i = 0; i < size; i++)
    for (int j = 0; j < size; j++)
    {
      if (!map.explored[i][j])
        cout << "*";
      else
      {
        if (map.value[i][j] == BOMB)
          cout << "x";
        else
          cout << map.value[i][j];
      }

      if (j == size - 1)
        cout << i << endl;
      else
        cout << " ";
    }
}

void inputAndValidatePosition(int &row, int &col, int size_map)
{
  do
  {
    cout << "Enter (row col): ";
    cin >> row >> col;

    if (!isValidPosition(row, col, size_map))
      cout << "Out of range or not valid, try again !\n";

  } while (!isValidPosition(row, col, size_map));
}

// What does this function do?
// reveal the map when selected
void exploreMapFromPosition(Map &map, int size, int row, int col)
{
  if (isValidPosition(row, col, size) && !map.explored[row][col])
  {
    map.explored[row][col] = true;
    explored_position++;
    if (map.value[row][col] == BOMB)
      return;

    if (map.value[row][col] == 0)
    {

      exploreMapFromPosition(map, size, row - 1, col - 1);
      exploreMapFromPosition(map, size, row - 1, col);
      exploreMapFromPosition(map, size, row - 1, col + 1);
      exploreMapFromPosition(map, size, row, col - 1);
      exploreMapFromPosition(map, size, row, col + 1);
      exploreMapFromPosition(map, size, row + 1, col - 1);
      exploreMapFromPosition(map, size, row + 1, col);
      exploreMapFromPosition(map, size, row + 1, col + 1);
    }
  }
}

int clickOnPosition(Map &map, int size, int choosen_row, int choosen_col)
{
  exploreMapFromPosition(map, size, choosen_row, choosen_col);
  if (map.value[choosen_row][choosen_col] == BOMB)
    return LOSE;

  if (explored_position == numberPositionExploredToWin)
    return WIN;
  else
    return PLAYING;
}

int main()
{
  int N, B, game_state, choosen_row, choosen_col;
  Map map;

  // What does do-while below do?
  // looping until input correct
  do
  {
    inputFieldAndBomb(N, B);

    if (B >= N * N)
      cout << "Error, number of bomb must less than N*N\n";
    else
    {
      initiateMap(map, N, B);
      cout << "Succesfully added\n";
    }

  } while (B >= N * N);

  explored_position = 0;
  numberPositionExploredToWin = N * N - B;

  // What does do-while below do?
  // enabling option to still playing (can click on map)
  do
  {
    printMap(map, N);
    inputAndValidatePosition(choosen_row, choosen_col, N);
    game_state = clickOnPosition(map, N, choosen_row, choosen_col);
  } while (game_state == PLAYING);

  printMap(map, N);

  if (game_state == WIN)
    cout << "Congrats, You WIN !\n";
  else
    cout << "Sorry, try again !\n";

  return 0;
}