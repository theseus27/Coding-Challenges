import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Problem1 {
    public static void main(String[] args) {
        ConsoleProcessor processor = new ConsoleProcessor();
        processor.processAllLines();
    }
}

class ConsoleProcessor {
    public OrgChart orgChart = new OrgChart();
    public void processAllLines() {
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        Integer numLines = 0;

        try {
           numLines = Integer.valueOf(line.trim());
        } catch (NumberFormatException ex) {
            ex.printStackTrace();
        }

        for (int i = 0; i < numLines; i++) {
            processLine(in.nextLine());
        }

        in.close();
    }

    protected void processLine(String line) {
        String[] parsedCommand = line.split(",");

        // ignore empty lines
        if (parsedCommand.length == 0) {
            return;
        }

        switch (parsedCommand[0]) {
            case "add":
                orgChart.add(parsedCommand[1], parsedCommand[2], parsedCommand[3]);
                break;
            case "print":
                orgChart.print();
                break;
            case "remove":
                orgChart.remove(parsedCommand[1]);
                break;
            case "move":
                orgChart.move(parsedCommand[1], parsedCommand[2]);
                break;
            case "count":
                System.out.println(orgChart.count(parsedCommand[1]));
                break;
        }
    }
}
class OrgChart {
    List<Employee> employees = new ArrayList<Employee>();
    
    class Employee {
        String id;
        String name;
        String managerId;
        List<Employee> reports = new ArrayList<Employee>();
        int level = 0;
        
        Employee(String i, String n, String m) {
            this.id = i;
            this.name = n;
            this.managerId = m;
        }
    }
    
    public Employee findEmployee(String emp) {
        for (Employee e : employees) {
            if (e.id.equals(emp)) {
                return e;
            }
        }
        return null;
    }
    
    public void add(String id, String name, String managerId)
    {
        if (findEmployee(id) != null) { return; }
        if (findEmployee(managerId) == null) { managerId = "-1"; }
        
        Employee added = new Employee(id, name, managerId);
        Employee manager = findEmployee(managerId);
        
        if (manager != null) { 
            manager.reports.add(added);
            added.level = manager.level + 1;
        }
        
        employees.add(added);
    }

    public void print()
    {
        List<Employee> topLevel = new ArrayList<Employee>();
        List<Employee> inOrder = new ArrayList<Employee>();
        
        for (Employee e : employees) {
            if (e.level == 0) {
                topLevel.add(e);
            }
        }
        
        for (Employee top : topLevel) {
            inOrder.add(top);
        }
        
        int idx = 0;
        while (idx < inOrder.size()) {
            Employee e = inOrder.get(idx);
            List<Employee> reps = new ArrayList<Employee>(e.reports);
            for (int y = 0; y < reps.size(); y++) {
                if (!inOrder.contains(reps.get(y))) {
                    inOrder.add(idx+y+1, reps.get(y));
                }
            }
            idx += 1;
        }
        
        for (Employee e : inOrder) {
            for (int i = 0; i < e.level; i++) { System.out.print("  "); }
            System.out.println(e.name + " [" + e.id + "]");
        }
    }

    public void remove(String employeeId)
    {
        Employee fired = findEmployee(employeeId);
        if (fired == null) { return; }
        
        Employee manager = findEmployee(fired.managerId);
        if (manager != null) {
            manager.reports.remove(fired);
        }
        
        for (Employee r : fired.reports) {
            r.level -= 1;
            r.managerId = fired.managerId;
            findEmployee(fired.managerId).reports.add(r);
        }
        
        employees.remove(fired);
    }

    public void move(String employeeId, String newManagerId)
    {
        if (findEmployee(employeeId) == null || findEmployee(newManagerId) == null) {
            return;
        }
        
        Employee moving = findEmployee(employeeId);
        Employee oldManager = findEmployee(moving.managerId);
        Employee newManager = findEmployee(newManagerId);
        if (oldManager != null) {
            oldManager.reports.remove(moving);
        }
        newManager.reports.add(moving);
        moving.managerId = newManagerId;
        moving.level = newManager.level + 1;
        
    }

    public int count(String employeeId)
    {
        int idx = 0;
        List<Employee> inOrder = new ArrayList<Employee>();
        inOrder.add(findEmployee(employeeId));
        
        while (idx < inOrder.size()) {
            Employee e = inOrder.get(idx);
            List<Employee> reps = new ArrayList<Employee>(e.reports);
            for (int y = 0; y < reps.size(); y++) {
                if (!inOrder.contains(reps.get(y))) {
                    inOrder.add(idx+y+1, reps.get(y));
                }
            }
            idx += 1;
        }
        
        return inOrder.size() - 1;
    }
}