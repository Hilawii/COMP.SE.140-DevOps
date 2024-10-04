package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os/exec"
	"strings"
	"fmt"
)

func makeSystemInfo(w http.ResponseWriter, r *http.Request) {
	ipAddress, _ := exec.Command("hostname", "-I").Output()
	runningProcesses, _ := exec.Command("ps", "-aux").Output()
	diskSpace, _ := exec.Command("df", "-h").Output()
	sinceLastBoot, _ := exec.Command("uptime", "-p").Output()

	systemInfo := map[string]string{
		"ip address":                strings.TrimSpace(string(ipAddress)),
		"list of running processes": strings.TrimSpace(string(runningProcesses)),
		"available disk space":      strings.TrimSpace(string(diskSpace)),
		"time since last boot":      strings.TrimSpace(string(sinceLastBoot)),
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(systemInfo)
}

func main() {
	http.HandleFunc("/", makeSystemInfo)
	fmt.Println("Server started on port 8200")
	log.Fatal(http.ListenAndServe(":8200", nil))
}
