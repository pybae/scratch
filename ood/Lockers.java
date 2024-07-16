/*
 * So let's see, pick up location
 * has a bunch of lockers, lockers have size as an attribute
 * size is an enum, or something
 *
 * a package has some function, based off its dimensions to figure out size,
 * relatively easy to do so
 *
 * on putting a package in, a code is produced for an item
 * package location can take the code to return the corresponding locker for it
 *
 * does a locker have a unique identifier?
 * eh i suppose so.
 *
 * yeah we should likely a db construct anyways 
 * is there information a locker needs to store as to its package?
 * probably not i think
 *
 * but can store whether its taken or not
 */

enum Size {
    SMALL(1, 2, 3),
    MEDIUM(2, 4, 6),
    LARGE(5, 7, 9);

    private final double width;
    private final double length;
    private final double height;

    private Size(double width, double length, double height) {
        this.width = width;
        this.length = length;
        this.height = height;
    }
}

class Locker {
    private final String id;
    private final Size size;
    private final boolean taken;

    public Locker(String id, Size size) {
        this.id = id;
        this.size = size;
        this.taken = false;
    }

    public Size getSize() {
        return this.size;
    }

    public boolean isTaken() {
        return this.taken;
    }

    public void claimLocker() {
        this.taken = true;
    }

    public void releaseLocker() {
        this.taken = false;
    }
}

class PickupLocation {
    private final Map<String, Locker> packageAssignments;
    private final Map<Size, List<Locker>> freeLockers;

    public PickupLocation(List<Locker> lockers) {
        this.packageAssignments = new HashMap<>();
        this.freeLockers = lockers.stream().collect(
                Collectors.toMap(ker::getSize, locker -> new ArrayList<>(locker), (l1, l2) -> l1.addAll(l2)));
    }

    public void openLocker(String code) {
        if (packageAssignments.containsKey(code)) {
            Locker locker = packageAssignemnts.get(code);
            locker.releaseLocker();
            this.freeLockers.get(locker.getSize()).append(locker);
        } else {
            throw new Exception("Attempted to open a locker with an invalid code!" + code);
        }
    }

    public Locker assignLocker(Package pkg) {
        Size size = getLockerSize(pkg);
        List<Locker> freeLockers = this.getLockerSize(pkg);
        Locker locker = freeLockers.pop();

        String code = this.generateCode();
        packageAssigments[code] = locker;
        locker.releaseLocker();

        return locker;
    }

    private Size getLockerSize(Package pkg) {
        for (Size size : Size.values()) {
            if (this.canFit(size, pkg) && this.freeLockers.get(size).size() > 0) {
                return size;
            }
        }
    }

    private boolean canFit(Size size, Package pkg) {
        // do the sorting thing
    }

    private String generateCode() {
        // do random generation plus collision detection, short string
        return "ASDF";
    }

}

class Package {
    private final String id;
    private final double width;
    private final double height;
    private final double length;

    public Package(String id, double width, double height, double length) {
        this.id = id;
        this.width = width;
        this.height = height;
        this.length = length;
    }

}
