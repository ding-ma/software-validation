import csv

import matplotlib.pyplot as plt


def readTime(fileName):
    iterations = []
    timeDifs = []
    startTimes = []
    endTimes = []

    with open(fileName, newline='') as f:
        next(f)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            iterations.append(int(row[0]))
            startTimes.append(float(row[1]))
            endTimes.append(float(row[2]))
            timeDifs.append(float(row[3]))

    return (iterations, startTimes, endTimes, timeDifs)


def getCPUandMem(fileName):
    iterations, startTimes, endTimes, _ = readTime(fileName)
    times = []
    cpuUsages = []
    memUsages = []

    for startTime, endTime in zip(startTimes, endTimes):
        with open("./test_data/system_logs.csv", newline='') as f:
            next(f)

            # [Time, CPU, Mem]
            closestBelow = None
            closestAbove = None

            reader = csv.reader(f, delimiter=',')
            for row in reader:

                sysTime = float(row[0])
                cpu = float(row[1])
                mem = float(row[3])

                if (cpu == 0):
                    continue

                if (closestBelow == None or (
                        startTime - sysTime > 0 and startTime - sysTime < startTime - closestBelow[0])):
                    closestBelow = [sysTime, cpu, mem]

                if (closestAbove == None and startTime - sysTime < 0):
                    closestAbove = [sysTime, cpu, mem]

            times.append(closestBelow[0])
            cpuUsages.append(closestAbove[1] - closestBelow[1])
            memUsages.append(closestAbove[1] - closestBelow[2])

    return (iterations, times, cpuUsages, memUsages)


def plotTimesT2(mode):
    categoryIterations, categoryStartTimes, _, categoryTimeDifs = readTime(
        './test_data/' + mode + '_category_time_stamps_t2.csv')
    todoIterations, todoStartTimes, _, todoTimeDifs = readTime('./test_data/' + mode + '_todo_time_stamps_t2.csv')
    projectIterations, projectStartTimes, _, projectTimeDifs = readTime(
        './test_data/' + mode + '_project_time_stamps_t2.csv')

    plt.figure()
    plt.plot(categoryIterations, categoryTimeDifs, label="Category")
    plt.plot(todoIterations, todoTimeDifs, label="Todo")
    plt.plot(projectIterations, projectTimeDifs, label="Project")

    plt.title(mode.capitalize() + ' T2 vs Number of Objects')
    plt.ylabel('T2 (seconds)')
    plt.xlabel('Number of Objects')
    plt.legend()
    plt.savefig('./graphs/T2_vs_numObj_for_' + mode.capitalize() + '.png')
    # plt.show()


def plotTimesT1(mode):
    categoryIterations, categoryStartTimes, _, categoryTimeDifs = readTime(
        './test_data/' + mode + '_category_time_stamps_t1.csv')
    todoIterations, todoStartTimes, _, todoTimeDifs = readTime('./test_data/' + mode + '_todo_time_stamps_t1.csv')
    projectIterations, projectStartTimes, _, projectTimeDifs = readTime(
        './test_data/' + mode + '_project_time_stamps_t1.csv')

    plt.figure()
    plt.plot(categoryIterations, categoryTimeDifs, label="Category")
    plt.plot(todoIterations, todoTimeDifs, label="Todo")
    plt.plot(projectIterations, projectTimeDifs, label="Project")

    plt.title(mode.capitalize() + ' T1 vs Number of Objects')
    plt.ylabel('T1 (seconds)')
    plt.xlabel('Number of Objects')
    plt.legend()
    plt.savefig('./graphs/T1_vs_numObj_for_' + mode.capitalize() + '.png')
    # plt.show()


def plotCPUandMem(mode):
    # Get data
    categoryIterations, categoryTimes, categoryCpuUsages, categoryMemUsages = getCPUandMem(
        './test_data/' + mode + '_category_time_stamps_t2.csv')
    todoIterations, todoTimes, todoCpuUsages, todoMemUsages = getCPUandMem(
        './test_data/' + mode + '_todo_time_stamps_t2.csv')
    projectIterations, projectTimes, projectCpuUsages, projectMemUsages = getCPUandMem(
        './test_data/' + mode + '_project_time_stamps_t2.csv')

    # Plot Mem vs Num Objects
    plt.figure()
    plt.plot(categoryIterations, categoryMemUsages, label="Category")
    plt.plot(todoIterations, todoMemUsages, label="Todo")
    plt.plot(projectIterations, projectMemUsages, label="Project")

    plt.title('Delta free memory vs number objects for ' + mode.capitalize())
    plt.xlabel('Number of objects')
    plt.ylabel('Delta free memory (bytes)')
    plt.legend()
    plt.savefig('./graphs/DeltaFreeMem_vs_numObj_for_' + mode + '.png')
    # plt.show()

    # Plot CPU vs Num Objects
    plt.figure()
    plt.plot(categoryIterations, categoryCpuUsages, label="Category")
    plt.plot(todoIterations, todoCpuUsages, label="Todo")
    plt.plot(projectIterations, projectCpuUsages, label="Project")

    plt.title('Delta CPU usage vs number objects for ' + mode.capitalize())
    plt.xlabel('Number of objects')
    plt.ylabel('CPU % Usage')
    plt.legend()
    plt.savefig('./graphs/DeltaCPU_vs_numObj_for_' + mode + '.png')
    # plt.show()

    # Plot Mem vs Sample Time
    plt.figure()
    plt.plot(categoryTimes, categoryMemUsages, label="Category")
    plt.plot(todoTimes, todoMemUsages, label="Todo")
    plt.plot(projectTimes, projectMemUsages, label="Project")

    plt.title('Delta free memory vs sample time for ' + mode.capitalize())
    plt.xlabel('Time (seconds)')
    plt.ylabel('Delta free memory (bytes)')
    plt.legend()
    plt.savefig('./graphs/DeltaFreeMem_vs_sampleTime_for_' + mode + '.png')
    # plt.show()

    # Plot CPU vs Sample Time
    plt.figure()
    plt.plot(categoryTimes, categoryCpuUsages, label="Category")
    plt.plot(todoTimes, todoCpuUsages, label="Todo")
    plt.plot(projectTimes, projectCpuUsages, label="Project")

    plt.title('Delta CPU usage vs sample time for ' + mode.capitalize())
    plt.xlabel('Time (seconds) ')
    plt.ylabel('Delta CPU % Usage')
    plt.legend()
    plt.savefig('./graphs/DeltaCPU_vs_sampleTime_for_' + mode + '.png')
    # plt.show()


plotCPUandMem("add")
plotCPUandMem("delete")
plotCPUandMem("change")

plotTimesT1("add")
plotTimesT1("delete")
plotTimesT1("change")

plotTimesT2("add")
plotTimesT2("delete")
plotTimesT2("change")
