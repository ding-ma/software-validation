import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def readTime(fileName):
    iterations = []
    timeDif = []
    startTime = []
    endTime = []

    with open(fileName, newline='') as f:
        next(f)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            iterations.append(int(row[0]))
            startTime.append(float(row[1]))
            endTime.append(float(row[2]))
            timeDif.append(float(row[3]))
    
    return (iterations, startTime, endTime, timeDif)

def getCPUandMem(fileName):
    iterations, startTimes, endTimes, timeDif = readTime(fileName)
    avgCPU = [] 
    avgMem = []
    
    for startTime, endTime in zip(startTimes, endTimes):
        with open("./test_data/system_logs.csv", newline='') as f:
            next(f)
            # closestTime = None
            # closestCpu = None
            # closestMem = None
            count = 0
            cpuUsages = 0
            memUsages = 0
            reader = csv.reader(f, delimiter=',')
            for row in reader:

                sysTime = float(row[0])

                # if (closestTime == None or abs(startTime - float(row[0]) < abs(startTime - closestTime))):
                #     closestTime = float(row[0])
                #     closestCpu = float(row[1])
                #     closestMem = float(row[2])

                if (sysTime >= startTime and sysTime <= endTime):
                    cpuUsages += float(row[1])
                    memUsages += float(row[2])
                    count += 1

            if (count == 0):
                avgCPU.append(0)
                avgMem.append(0)
            else:
                avgCPU.append(cpuUsages/count)
                avgMem.append(memUsages/count)
    
    return (iterations, avgCPU, avgMem)

def plotTimes(timeType, mode):
    deleteCategoryIterations, _, _, deleteCategoryT1 = readTime('./test_data/' + mode + '_category_time_stamps_' + timeType + '.csv')
    deleteTodoIterations, _, _, deleteTodoT1 = readTime('./test_data/' + mode + '_todo_time_stamps_' + timeType + '.csv')
    deleteProjectIterations, _, _, deleteProjectT1 = readTime('./test_data/' + mode + '_Project_time_stamps_' + timeType + '.csv')

    plt.figure()
    plt.plot(deleteCategoryIterations, deleteCategoryT1, label = "Category")
    plt.plot(deleteTodoIterations, deleteTodoT1, label = "Todo")
    plt.plot(deleteProjectIterations, deleteProjectT1, label = "Project")

    plt.title(mode.capitalize() + ' time ' + timeType.capitalize())
    plt.ylabel('Time')
    plt.xlabel('Iteration')
    plt.legend()
    plt.savefig('./graphs/' + mode + ' ' + timeType + 's.png')
    # plt.show()

def plotCPUandMemTimes(timeType, mode):
    categoryIterations, categoryCpuUsages, categoryMemUsages = getCPUandMem('./test_data/' + mode + '_category_time_stamps_' + timeType + '.csv')
    todoIterations, todoCpuUsages, todoMemUsages = getCPUandMem('./test_data/' + mode + '_todo_time_stamps_' + timeType + '.csv')
    projectIterations, projectCpuUsages, projectMemUsages = getCPUandMem('./test_data/' + mode + '_project_time_stamps_' + timeType + '.csv')

    plt.figure()
    plt.plot(categoryIterations, categoryCpuUsages, label = "Category")
    plt.plot(todoIterations, todoCpuUsages, label = "Todo")
    plt.plot(projectIterations, projectCpuUsages, label = "Project")

    plt.title('CPU usage over ' + timeType.capitalize() + ' for ' + mode.capitalize())
    plt.xlabel('Iteration')
    plt.ylabel('CPU % Use')
    plt.legend()
    plt.savefig('./graphs/CPU ' + mode + ' ' + timeType + 's.png')
    # plt.show()

    plt.figure()
    plt.plot(categoryIterations, categoryMemUsages, label = "Category")
    plt.plot(todoIterations, todoMemUsages, label = "Todo")
    plt.plot(projectIterations, projectMemUsages, label = "Project")

    plt.title('Memory usage over ' + timeType.capitalize() + ' for ' + mode.capitalize())
    plt.xlabel('Iteration')
    plt.ylabel('Memory Use (bytes)')
    plt.legend()
    plt.savefig('./graphs/Mem ' + mode + ' ' + timeType + 's.png')
    # plt.show()

timeTypes = ["t1", "t2"]
modes = ["add", "change", "delete"]

for timeType in timeTypes:
    for mode in modes:
        plotTimes(timeType, mode)
        plotCPUandMemTimes(timeType, mode)