package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"strings"
)

/*
 * Complete the 'formingMagicSquare' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY s as parameter.
 */

// func formingMagicSquare(s [][]int32) int32 {
// 	// Write your code here

// }
func completeMatrix(s [][]int32) ([][]int32, error) {
	check := make([]bool, 10)
	check[0] = true
	check[5] = true
	s[0][2] = 15 - s[0][0] - s[0][1]
	if s[0][2] > 9 {
		return s, errors.New("error")
	}
	check[s[0][2]] = true
	for i := 0; i < 3; i++ {
		s[2][i] = 10 - s[0][2-i]
		if s[2][i] > 9 {
			return s, errors.New("error")
		}
		check[s[2][i]] = true
	}
	s[1][0] = 15 - s[0][0] - s[2][0]
	if s[1][0] > 9 {
		return s, errors.New("error")
	}
	check[s[1][0]] = true
	s[1][2] = 15 - s[0][2] - s[2][2]
	if s[1][2] > 9 {
		return s, errors.New("error")
	}
	check[s[1][2]] = true

	for i := 1; i < 10; i++ {
		if !check[i] {
			return s, errors.New("error")
		}
	}
	return s, nil

}

func formingMagicSquare() {
	// Write your code here
	check := make([]bool, 10)
	check[0] = true
	check[5] = true
	s := [][]int32{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	s[1][1] = 5
	for i := 1; i < 10; i++ {
		if !check[i] {
			s[0][0] = int32(i)
			check[i] = true
			for j := 1; j < 10; i++ {
				if !check[j] {
					s[0][1] = int32(j)
					check[j] = true
					matrix, err := completeMatrix(s)
					if err == nil {
						fmt.Println(matrix)
					}
					check[j] = false
				}
			}
			check[i] = false
		}
	}

}

func main() {
	// reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	// stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	// checkError(err)

	// defer stdout.Close()

	// writer := bufio.NewWriterSize(stdout, 16*1024*1024)
	// var matrix [3][3]int8

	// // Tạo một đối tượng scanner để đọc dữ liệu từ bàn phím
	// scanner := bufio.NewScanner(os.Stdin)

	// // Duyệt qua từng dòng của input
	// for i := 0; i < 3; i++ {
	//     // Đọc một dòng từ scanner
	//     if !scanner.Scan() {
	//         // Nếu không đọc được dòng, thoát khỏi vòng lặp
	//         break
	//     }
	//     line := scanner.Text()

	//     // Tách các phần tử trên dòng bằng dấu cách
	//     parts := strings.Split(line, " ")

	//     // Chuyển các phần tử từ kiểu chuỗi sang kiểu số nguyên và lưu vào ma trận
	//     for j, part := range parts {
	//         num, _ := strconv.Atoi(part)
	//         matrix[i][j] = int8(num)

	//     }
	// }

	// In ra ma trận đã đọc được
	formingMagicSquare()

	// result := formingMagicSquare(s)

	// fmt.Fprintf(writer, "%d\n", result)

	// writer.Flush()
	// formingMagicSquare(s)
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err == io.EOF {
		return ""
	}

	return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
	if err != nil {
		panic(err)
	}
}
