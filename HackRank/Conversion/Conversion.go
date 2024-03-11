package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

/*
 * Complete the 'timeConversion' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

func timeConversion(s string) string {
	// Write your code here
	var hour, min, sec, ampm string
	hour = s[0:2]
	min = s[3:5]
	sec = s[6:8]
	ampm = s[8:10]

	h, err := strconv.Atoi(hour)
	checkError(err)
	if ampm == "PM" {

		if h < 12 {
			hour = strconv.Itoa(h + 12)
		}

	} else {
		if h >= 12 {
			hour = strconv.Itoa(h - 12)
		}
	}
	if len(hour) == 1 {
		hour = "0" + hour
	}
	return hour + ":" + min + ":" + sec

}

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 16*1024*1024)

	// stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
	// checkError(err)

	// defer stdout.Close()

	// writer := bufio.NewWriterSize(stdout, 16*1024*1024)

	s := readLine(reader)

	result := timeConversion(s)

	fmt.Println(result)

	// fmt.Fprintf(writer, "%s\n", result)

	// writer.Flush()
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
