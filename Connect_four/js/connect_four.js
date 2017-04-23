$(function(){

  //2d array for the board
  // var gameBoard = Array(6).fill(Array(7).fill(''));
  gameBoard = new Array(6)
  for (var i = 0; i < gameBoard.length; i++) {
    gameBoard[i] = new Array(7);
  }
  for (var i = 0; i < gameBoard.length; i++) {
    for (var j = 0; j < gameBoard[i].length; j++) {
      gameBoard[i][j] = '0'
    }
  }
  var rows = 6;
  var cols = 7;
  var chipsTotal = rows * cols;

  //initiate the board
  function initBoard(){
  var chip = "<td class='chip'><div class='circleShape circleInitial'> </div></td>";
  var chips = Array(cols).fill(chip);
  chips = "<tr>" + chips + "/tr";
  $('#board').html(Array(rows).fill(chips));
  for (var i = 0; i < chipsTotal; i++) {
    var col='col' + (i%cols).toString();
    var row='row' + (~~(i/cols)).toString()
    $('.chip > div').eq(i).addClass(col).addClass(row);
  };
  };

  // get players names
  var gotPlayerOne = false;
  while (!gotPlayerOne) {
    playerOne = prompt('Player One: Enter Your Name , you will be Blue')
    if (playerOne !== '') {
      gotPlayerOne = true
    }
  };
  var gotPlayerTwo = false;
  while (!gotPlayerTwo) {
    playerTwo = prompt('Player Two: Enter Your Name , you will be Red')
    if (playerTwo !== '') {
      gotPlayerTwo = true
    }
  };

  initBoard();

  // set variables
  var circlePlayerOne = 'circlePlayerOne';
  var chipPlayerOne = '1';
  var winPlayerOne = '1111';

  var circlePlayerTwo = 'circlePlayerTwo';
  var chipPlayerTwo = '2';
  var winPlayerTwo = '2222';

  // implement game logics
  var gotWinner = false;
  while (!gotWinner) {
    //for playerOne
    $('#status').html(playerOne + ': it is your turn, please pick a column to drop your blue chip');
    $('#status').css('visibility', 'visible');
    makeTurn(circlePlayerOne, chipPlayerOne);
    gotWinner = checkWinner(winPlayerOne);
    if (gotWinner) {
      break;
    };

    //for playerTwo
    $('#status').html(playerTwo + ': it is your turn, please pick a column to drop your red chip');
    $('#status').css('visibility', 'visible');
    makeTurn(circlePlayerTwo, chipPlayerTwo);
    gotWinner = checkWinner(winPlayerTwo);
    if (gotWinner) {
      break;
    };

  };

  $('#status').html('Game was won');

  function makeTurn (circleClass, chipSymbol) {
  var prev = $(NaN);
  $('table#board').on('click', '.circleShape', (function (){
  prev.css('border', '2px solid white');
  prev = $(this).closest('.chip');
  prev.css('border', '3px solid #1628ad');
  var index = $(this).attr('class').indexOf('col');
  var col = '.' + $(this).attr('class').substr(index, 4);
  for (var i = (rows-1); i >=0 ; i--) {
    row = '.row' + i.toString();
    if ($(col+row).hasClass('circleInitial')) {
      $(col+row).removeClass('circleInitial').addClass(circleClass);
      var rowInd = Number(row[4]);
      var colInd = Number(col[4]);
      if (gameBoard[rowInd][colInd] === '0') {
        gameBoard[rowInd][colInd] = chipSymbol
      }
      break;
    }
  }}))
  };

  function checkWinner (winString) {
    var gotWinner = false;
    for (var i = 0; i < gameBoard.length; i++) {
      currentString = gameBoard[i].join('');
      if (currentString.indexOf(winString) !== -1) {
        gotWinner = true;
        break;
      }
    }
    return gotWinner;
  }

  // get ann array for all dimensions
  function makeAllDimensionsArray(gameBoard){
    //add horisontals
    var allDimensionsArray = gameBoard;
    //add  verticals
    var allDimensionsArray = allDimensionsArray.concat(
       gameBoard[0].map(function(col, i){
      return gameBoard.map(function(row){
        return row[i];
      });
    }));
    //add diagonals
    function getAllDiagonal(gameBoard, bottomToTop) {
      var Ylength = gameBoard.length;
      var Xlength = gameBoard[0].length;
      var maxLength = Math.max(Xlength, Ylength);
      var temp;
      var diagonalArray = [];
      for (var k = 0; k <= 2 * (maxLength - 1); ++k) {
        temp = [];
        for (var y = Ylength - 1; y >= 0; --y) {
          var x = k - (bottomToTop ? Ylength - y : y);
          if (x >= 0 && x < Xlength) {
              temp.push(gameBoard[y][x]);
          }
        }
        if(temp.length > 3) {
            diagonalArray.push(temp);
        }
      }
      return diagonalArray;
    };
    allDimensionsArray = allDimensionsArray.concat(getAllDiagonal(gameBoard, false));
    allDimensionsArray = allDimensionsArray.concat(getAllDiagonal(gameBoard, true));
    return allDimensionsArray;
  };


  // var previous = $(NaN);
  // $('table#board').on('click', '.circleShape', (function(){
  //   previous.css('border', '2px solid white');
  //   previous = $(this).closest('.chip');
  //   previous.css('border', '3px solid #1628ad');
  //   var index = $(this).attr('class').indexOf('col');
  //   var col = '.' + $(this).attr('class').substr(index, 4);
  //   for (var i = (rows-1); i >=0 ; i--) {
  //     row = '.row' + i.toString();
  //     if ($(col+row).hasClass('circleInitial')) {
  //       $(col+row).removeClass('circleInitial').addClass('circlePlayerOne');
  //       var rowInd = Number(row[4]);
  //       var colInd = Number(col[4]);
  //       if (gameBoard[rowInd][colInd] === '0') {
  //         gameBoard[rowInd][colInd] ='1'
  //       }
  //       break;
  //     }
  //   }
  // }));


})
