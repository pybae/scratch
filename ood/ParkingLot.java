class Spot {
    private final String id;
    private long takenTimestamp;
    private boolean taken;

    public Spot(String id) {
        this.id = id;
        this.takenTimestamp = -1;
        this.taken = false;
    }

    public void claimSpot() {
        this.taken = true;
        this.takenTimestamp = System.currentTimeMillis();
    }
}

class Floor {
    private final String id; // could be an int
    private final List<Spot> spots;

    public Floor(String id, List<Spot> spots) {
        this.id = id;
        this.spots = ImmutableList.copyOf(spots);
    }
}

class Location {
    private final Floor floor;
    private final int row;
    private final int column;

    public Location(Floor floor, int row, int column) {
        this.floor = floor;
        this.row = row;
        this.column = column;
    }
}

class Lot {
    private final PriorityQueue<Location, Spot> availableSpots;
    private final List<Floor> allFloors;

    public Lot(List<Floor> allFloors) {
        this.allFloors = allFloors;
        this.availableSpots = new PriorityQueue<>();
        for (Floor floor : allFloors) {
            for (Spot spot : allSpots) {
                this.availableSpots.add(spot);
            }
        }
    }

    public Spot getClosestSpot() {
        if (this.availableSpots.size() == 0) {
            throw new Exception("No available spots!")
        } 
        Spot spot = availableSpots.pop();
        spot.claimSpot();
        return spot;
    }

    public 
}
